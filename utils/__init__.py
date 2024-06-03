class ClippingUtils:
    def __init__(self):
        pass

    def main_function(self):
        for book in book_highlights:
            try:
                existing_pages = getting_existing_pages_info()
                if book in existing_pages:
                    pass
                else:
                    create_new_book_page(
                        book
                    )  # Creating a page for a new book in Notion when the book doesn't already exist.
                    existing_pages = getting_existing_pages_info()
                for highlight in book_highlights[book]:
                    add_blocks_to_page(highlight, existing_pages[book])
                    if book_highlights[book][highlight] != None:
                        add_blocks_to_page(
                            book_highlights[book][highlight],
                            existing_pages[book],
                            is_note=True,
                        )
            except:
                print(
                    f"{RED_COLOR}An error occurred! \nPlease make sure the IDs are correct! Access them by opening user-info.json{RESET_COLOR}"
                )
                if LATEST_API_STATUS:
                    print(
                        f"{RED_COLOR}Error Information! \nStatus Code -> {LATEST_API_STATUS}\nAPI Error -> {LATEST_API_TEXT}{RESET_COLOR}"
                    )
                time.sleep(5)
                exit()
        print(
            f"{GREEN_COLOR}Successfully Finished Adding the Highlights! \nLearn and Enjoy!!! :){RESET_COLOR}"
        )
        success_rate = SUCCESS / TOTAL * 100
        fail_rate = FAIL / TOTAL * 100
        print(
            f"{GREEN_COLOR}Success: {success_rate}%{RESET_COLOR} \n{RED_COLOR}Fail: {fail_rate}%{RESET_COLOR}"
        )
