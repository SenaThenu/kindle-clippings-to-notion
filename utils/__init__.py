import time

from .extract_clippings import extractor
from .notion_api_handler import NotionApiHandler


def extract_and_upload_clippings(
    config_manager: object,
    update_progress_signal: object,
    update_status_message_signal: object,
):
    """
    Extracts the clippings from My Clippings.txt and uploads them to the given notion database!

    Args:
        config_manager (object)
        update_progress_signal (object)
        update_status_message_signal (object)
    """
    # extracting the clippings
    update_status_message_signal.emit("Extracting the clippings from the text file...")
    clippings_dict = extractor(config_manager.config["SELECTED_PATH"])
    update_progress_signal.emit(20)

    update_status_message_signal.emit("Uploading to Notion")
    # uploading them to notion
    notion_uploader = NotionApiHandler(config_manager)
    notion_uploader.upload_clippings(clippings_dict)
    update_progress_signal.emit(100)
    time.sleep(3)
