import sys
from PyQt6.QtWidgets import QApplication

import gui
from config import ConfigManager
from utils import extract_and_upload_clippings

config_manager = ConfigManager()

if __name__ == "__main__":
    # configuring lower level stuff
    app = QApplication(sys.argv)

    # binding the ui
    main_gui = gui.create_gui(config_manager, extract_and_upload_clippings)

    # showing it to the users
    main_gui.show()

    # closing the browser window when quitting
    sys.exit(app.exec())
