from .extract_clippings import extractor
from .notion_api_handler import NotionApiHandler


def extract_and_upload_clippings(config_manager: object):
    """
    Extracts the clippings from My Clippings.txt and uploads them to the given notion database!

    Args:
        config_manager (object)
    """
    # extracting the clippings
    clippings_dict = extractor(config_manager.config["SELECTED_PATH"])

    # uploading them to notion
    notion_uploader = NotionApiHandler(config_manager)
    notion_uploader.upload_clippings(clippings_dict)
