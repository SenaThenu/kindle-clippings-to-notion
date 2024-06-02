"""
Connects the GUI and the Utils
"""

from os import path
from functools import partial

from PyQt6 import QtWidgets, QtGui
from ._main_ui import Ui_mainWindow
from ._credentials_ui import Ui_Credentials

MAIN_GUI = Ui_mainWindow()
CREDENTIALS_GUI = Ui_Credentials()

LOGO_PATH = path.abspath(
    path.join(path.dirname(path.dirname(__file__)), "readme_assets/app_logo.png")
)

# Class instances that provides access to program functions
CREDENTIALS_MANAGER = None


def create_gui(credential_manager: object):
    # globalising the main objects passed into the function
    global CREDENTIALS_MANAGER
    CREDENTIALS_MANAGER = credential_manager

    # binding the qt-generated UI
    main_window = QtWidgets.QMainWindow()
    MAIN_GUI.setupUi(main_window)

    # sets up UI elements
    _setup_menubar()

    # basic main window configurations
    main_window.setWindowIcon(QtGui.QIcon(LOGO_PATH))
    return main_window


def _setup_menubar():
    """
    Makes the menu bar of the main window functional
    """
    MAIN_GUI.actionCredentials.triggered.connect(_configure_credentials_editor)


def _set_up_credentials_editor_functions():
    """
    Makes the UI elements in the credentials editor functional
    """
    # storing references to the 2 input objects
    database_id_input = CREDENTIALS_GUI.databaseIdInput
    notion_token_input = CREDENTIALS_GUI.notionAuthTokenInput

    # showing the current values
    database_id_input.setText(CREDENTIALS_MANAGER.credentials["BOOK_DB_ID"])
    notion_token_input.setText(CREDENTIALS_MANAGER.credentials["NOTION_TOKEN"])

    # hiding some stuff
    CREDENTIALS_GUI.savedMessageLabel.setHidden(True)

    # enabling the saving button
    def _save_credentials():
        CREDENTIALS_MANAGER.save_credentials(
            book_id=database_id_input.text(),
            notion_token=notion_token_input.text(),
        )

        # showing the success message
        CREDENTIALS_GUI.savedMessageLabel.setHidden(False)

    CREDENTIALS_GUI.saveBtn.clicked.connect(_save_credentials)


def _configure_credentials_editor():
    """
    Creates the interface for the users to edit their credentials
    """
    # binding the qt-generated UI
    credentials_dialog = QtWidgets.QDialog()
    CREDENTIALS_GUI.setupUi(credentials_dialog)

    # configuring the UI
    credentials_dialog.setWindowTitle("Hashtags Editor")
    credentials_dialog.setWindowIcon(QtGui.QIcon(LOGO_PATH))
    _set_up_credentials_editor_functions()

    # displaying the UI
    credentials_dialog.exec()
    credentials_dialog.show()
