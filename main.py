import sys
from PyQt6.QtWidgets import QApplication

import gui
from config import CredentialManager

credential_manager = CredentialManager()

if __name__ == "__main__":
    # configuring lower level stuff
    app = QApplication(sys.argv)

    # binding the ui
    main_gui = gui.create_gui(credential_manager)

    # showing it to the users
    main_gui.show()

    # closing the browser window when quitting
    sys.exit(app.exec())
