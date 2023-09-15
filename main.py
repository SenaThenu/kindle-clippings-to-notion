import requests
import json
import art
import time

# Global color variables
RED_COLOR = "\033[31m"
GREEN_COLOR = "\033[32m"
BLUE_COLOR = "\033[34m"
YELLOW_COLOR = "\033[33m"
PURPLE_COLOR = "\033[35m"
RESET_COLOR = "\033[0m"

LATEST_API_STATUS = None
LATEST_API_TEXT = None

# Some counters
TOTAL = 0
SUCCESS = 0
FAIL = 0

with open("user-info.json", "r") as user_f:
    # Loading the ids
    user_info = json.load(user_f)

# ID definitions
API_ID = user_info["API_ID"]
DATABASE_ID = user_info["BOOK_DB_ID"]

def get_valid_input(prompt):
    """Validates user inputs"""
    valid_input = False
    
    while not valid_input:
        answer = input(prompt).strip()
        if not answer:  # Checking whether the answer is blank
            print(f"{RED_COLOR}Don't leave this blank!{RESET_COLOR}")
            continue
        else:
            valid_input = True
    
    return answer

def update_ids():
    """This updates the user IDs in user.json"""
    global API_ID, DATABASE_ID
    new_ids = {}

    print(f"{BLUE_COLOR}Before we begin, you have to enter the following IDs. \nRead this to find your IDs: https://github.com/SenaThenu?tab=repositories {RESET_COLOR}\n{RED_COLOR}Note: These will be stored on your local computer. So, you have to enter only once! (Can be changed through user-info.json!){RESET_COLOR}")
    
    api_id = get_valid_input("Enter you API ID (integration secret key): ")
    book_db_id = get_valid_input("Enter the Database ID to save Kindle Clippings: ")
    
    new_ids["API_ID"] = api_id
    new_ids["BOOK_DB_ID"] = book_db_id
    with open("user-info.json", "w") as user_edit:
        json.dump(new_ids, user_edit)

    API_ID = api_id
    DATABASE_ID = book_db_id

def count_response(status):
    global SUCCESS, FAIL, TOTAL
    if status == 200:
        SUCCESS += 1
    else:
        FAIL += 1
    TOTAL += 1

def extract_the_clippings():
    """This returns a dictionary which contains all the highlights under the book name. The notes are assigned to the key highlight!"""
    books = {}

    # Retrieving from my clippings
    with open("My Clippings.txt", "r", encoding="utf8") as f:
        raw_bulk = f.readlines()

    for i, line in enumerate(raw_bulk):
        if line[:2] == "- ":
            book_name = raw_bulk[i-1]
            if book_name not in books:
                books[book_name] = {}
            else:
                pass
            content_type = line[7]    # H-Highlight, N-Note and B-Bookmarks
            if content_type == "H":
                # The content is i+2
                books[book_name][raw_bulk[i+2][:-2]] = None
            elif content_type == "N":
                highlight_bound = {list(books[book_name])[-1]: raw_bulk[i+2][:-1]}  # This binds the note with the previous highlight
                books[book_name].update(highlight_bound)
            else:
                pass
        else:
            pass
    return books

def getting_existing_pages_info():
    """This returns a dictionary of existing pages on notion with key value pairs as {book_name: book_id}"""
    global LATEST_API_STATUS, LATEST_API_TEXT

    request_url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.request("POST", request_url, headers=HEADERS)
    response_dict = json.loads(response.text)
    existing_page_info_list = response_dict['results']
    
    LATEST_API_STATUS = response.status_code
    LATEST_API_TEXT = response.text

    page_info = {}
    for info in existing_page_info_list:
        # this is the index: ["properties"]["Name"]["title"][0]["plain_text"]
        book_name = info["properties"]["Name"]["title"][0]["plain_text"]
        book_id = info["id"]
        page_info[book_name] = book_id
    return page_info

def create_new_book_page(book_name):
    """This creates a new book page"""
    global LATEST_API_STATUS, LATEST_API_TEXT

    request_url = "https://api.notion.com/v1/pages"

    raw_book_data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {
                "type": "title",
                "title": [{"type": "text", "text": {"content": book_name}}],
            },
        }
    }

    book_data = json.dumps(raw_book_data)
    response = requests.request("POST", request_url, headers=HEADERS, data=book_data)
    
    LATEST_API_STATUS = response.status_code
    LATEST_API_TEXT = response.text

    count_response(response.status_code)

def add_blocks_to_page(content, book_page_id, is_note=False):
    """This adds a piece of content to a page!"""
    request_url = f"https://api.notion.com/v1/blocks/{book_page_id}/children"

    if is_note:
        to_save_type = "bulleted_list_item"
    else:
        to_save_type = "paragraph"
    raw_data = {
        "children": [
            {
                "object": "block",
                "type": to_save_type,
                to_save_type: {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content,
                            }
                        }
                    ]
                }
            }
        ]
    }

    block_data = json.dumps(raw_data)
    response = requests.request("PATCH", request_url, headers=HEADERS, data=block_data)
    count_response(response.status_code)

art.tprint("Kindle Clippings to Notion!", font="small")
print(f"{PURPLE_COLOR}Please make sure you have pasted \"My Clippings.txt\" file in this folder!{RESET_COLOR} \n{YELLOW_COLOR}This program is sensitive to the filename... :){RESET_COLOR}")
input(f"{GREEN_COLOR}Press Enter to Begin: {RESET_COLOR}")

if not API_ID or not DATABASE_ID:   # Checking whether the IDs are empty
    update_ids()
else:
    pass

HEADERS = {
    "Authorization": f"Bearer {API_ID}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

print(f"{GREEN_COLOR}Started Extracting Kindle Clippings!{RESET_COLOR}")
book_highlights = extract_the_clippings()
print(f"{GREEN_COLOR}Finished Extracting Kindle Clippings!")

print(f"{GREEN_COLOR}Started Adding the Clippings to Notion{RESET_COLOR}")
for book in book_highlights:
    try:
        existing_pages = getting_existing_pages_info() 
        if book in existing_pages:
            pass
        else:
            create_new_book_page(book) # Creating a page for a new book in Notion when the book doesn't already exist.
            existing_pages = getting_existing_pages_info()
        for highlight in book_highlights[book]:
            add_blocks_to_page(highlight, existing_pages[book])
            if book_highlights[book][highlight] != None:
                add_blocks_to_page(book_highlights[book][highlight], existing_pages[book], is_note=True)
    except:
        print(f"{RED_COLOR}An error occurred! \nPlease make sure the IDs are correct! Access them by opening user-info.json{RESET_COLOR}")
        if LATEST_API_STATUS:
            print(f"{RED_COLOR}Error Information! \nStatus Code -> {LATEST_API_STATUS}\nAPI Error -> {LATEST_API_TEXT}{RESET_COLOR}")
        time.sleep(5)
        exit()
print(f"{GREEN_COLOR}Successfully Finished Adding the Highlights! \nLearn and Enjoy!!! :){RESET_COLOR}")
success_rate = SUCCESS/TOTAL * 100
fail_rate = FAIL/TOTAL * 100
print(f"{GREEN_COLOR}Success: {success_rate}%{RESET_COLOR} \n{RED_COLOR}Fail: {fail_rate}%{RESET_COLOR}")