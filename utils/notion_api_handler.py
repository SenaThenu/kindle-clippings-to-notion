import requests
import json


class NotionApiHandler:
    def __init__(self, config_manager: object):
        """
        Handles all the API calls to the Notion API and clippings uploading functionality

        Args:
            config_manager (object)
        """
        # credentials + authorization handling
        self.book_db_id = config_manager.config["BOOK_DB_ID"]
        self.notion_auth_token = config_manager.config["NOTION_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {self.notion_auth_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

        # internal attributes to make the class functional
        self._existing_book_pages = self._get_existing_book_pages()

    def _get_existing_book_pages(self) -> dict:
        """
        Retrieves the pages in the book_db and pairs up each book name with its corresponding id in a dictionary

        Returns:
            dict: key is the book name and its id is the value
        """
        request_url = f"https://api.notion.com/v1/databases/{self.book_db_id}/query"
        response = requests.request("POST", request_url, headers=self.headers)
        response_dict = json.loads(response.text)
        existing_page_info_list = response_dict["results"]

        # extracting the book name and its page id
        page_info = {}
        for info in existing_page_info_list:
            # this is the index: ["properties"]["Name"]["title"][0]["plain_text"]
            book_name = info["properties"]["Name"]["title"][0]["plain_text"]
            book_id = info["id"]
            page_info[book_name] = book_id

        return page_info

    def _create_new_book_page(
        self,
        book_name: str,
        author: str,
    ):
        """
        Creates a new page in the books database and adds its id to existing book pages

        Args:
            book_name (str): name of the book
            author (str): name of the author
        """
        request_url = "https://api.notion.com/v1/pages"

        raw_book_data = {
            "parent": {"database_id": self.book_db_id},
            "icon": {"emoji": "✨"},
            "properties": {
                "Name": {
                    "title": [{"text": {"content": book_name}}],
                },
                "Author": {"rich_text": [{"text": {"content": author}}]},
                "Highlights": {"number": 0},
                "Format": {"select": {"name": "eBook"}},
            },
        }

        book_data = json.dumps(raw_book_data)
        response = requests.request(
            "POST", request_url, headers=self.headers, data=book_data
        ).text

        response = json.loads(response)

        if response["object"] == "error":
            # this is possible when either of the properties doesn't exist
            # in such a case, we will just add only the book name and the icon
            raw_book_data["properties"] = {"Name": raw_book_data["properties"]["Name"]}
            book_data = json.dumps(raw_book_data)

            response = requests.request(
                "POST", request_url, headers=self.headers, data=book_data
            ).text
            response = json.loads(response)

        # adding the new page to existing book pages
        self._existing_book_pages[book_name] = response["id"]

    def _add_a_block_to_page(
        self,
        content: str,
        book_page_id: str,
        is_date: bool = False,
        is_note: bool = False,
    ):
        """
        Adds a block to the given page id

        Args:
            content (str): the text inside the block
            book_page_id (str): the id of the page
            is_date (bool, optional): whether the block contains the date the clipping was added. Defaults to False.
            is_note (bool, optional): whether the block contains a note by the user. Defaults to False.
        """
        request_url = f"https://api.notion.com/v1/blocks/{book_page_id}/children"

        if is_note:
            to_save_type = "bulleted_list_item"
        else:
            to_save_type = "paragraph"

        # additional stuff based on the block type
        annotation = {"italic": True} if is_date else {}
        content = f"Your Note: " if is_note else content

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
                                },
                                "annotations": annotation,
                            }
                        ]
                    },
                }
            ]
        }

        block_data = json.dumps(raw_data)
        response = requests.request(
            "PATCH", request_url, headers=self.headers, data=block_data
        )

    def upload_clippings(self, clippings_dict: dict):
        for book_name, clippings_list in clippings_dict:
            if book_name not in self._existing_book_pages.keys():
                self._create_new_book_page(
                    book_name=book_name, author=clippings_list[0]["author"]
                )
            
            current_book_page_id = self._existing_book_pages[book_name]

            for i, clipping in enumerate(clippings_list):
                # highlight
                self._add_a_block_to_page(clipping["highlight"], current_book_page_id)

                if clipping["note"]:
                    # if a note exists
                    self._add_a_block_to_page(clipping["note"], current_book_page_id, is_note=True)

                # location and the added date
                self._add_a_block_to_page(f"On Page {clipping["page"]} | {clipping["added_datetime"]}", current_book_page_id, is_date=True)

                # adding a blank block to separate different clippings
                if i < len(clippings_list) - 1:
                    self._add_a_block_to_page("", current_book_page_id)
