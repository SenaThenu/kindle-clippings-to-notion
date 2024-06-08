import time
import math

from .extract_clippings import extractor
from .notion_api_handler import NotionApiHandler


def extract_and_upload_clippings(
    config_manager: object,
    display_error_message: object,
    update_progress_signal: object,
    update_status_message_signal: object,
):
    """
    Extracts the clippings from My Clippings.txt and uploads them to the given notion database!

    Args:
        config_manager (object)
        display_error_message (object): callback used to display an error!
        update_progress_signal (object)
        update_status_message_signal (object)
    """
    # some in-function variables
    _progress_after_extracting_clippings = 20

    # extracting the clippings
    update_status_message_signal.emit("Extracting the clippings from the text file...")
    clippings_dict, n_total_clippings = extractor(
        config_manager.config["SELECTED_PATH"]
    )
    update_progress_signal.emit(_progress_after_extracting_clippings)

    try:
        if n_total_clippings > 0:
            # uploading them to notion
            progress_increment_for_each_upload = math.floor(80 / n_total_clippings)

            update_status_message_signal.emit("Getting Ready to Upload to Notion")
            notion_uploader = NotionApiHandler(
                config_manager,
                update_progress_signal,
                update_status_message_signal,
                _progress_after_extracting_clippings,
                progress_increment_for_each_upload,
            )
            notion_uploader.upload_clippings(clippings_dict)
            update_progress_signal.emit(100)
            time.sleep(1)
    except:
        display_error_message(
            "An error occurred :( \n1. Make sure your credentials are correct\n2. Check whether the correct file is provided!"
        )
        raise Exception("Error!")
