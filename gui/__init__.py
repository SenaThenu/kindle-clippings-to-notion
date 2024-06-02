from os import path
from PyQt6 import QtWidgets, QtGui
from ._main_ui import Ui_mainWindow
from ._credentials_ui import Ui_Credentials

MAIN_GUI = Ui_mainWindow()
CREDENTIALS_GUI = Ui_Credentials()

LOGO_PATH = path.abspath(
    path.join(path.dirname(path.dirname(__file__)), "readme_assets/app_logo.png")
)


def create_gui():
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
    MAIN_GUI.actionCredentials.triggered.connect(_open_credentials_editor)


def _open_credentials_editor():
    """
    Creates the interface for the users to edit their credentials
    """
    # binding the qt-generated UI
    credentials_dialog = QtWidgets.QDialog()
    CREDENTIALS_GUI.setupUi(credentials_dialog)

    # configuring the UI
    credentials_dialog.setWindowTitle("Hashtags Editor")
    credentials_dialog.setWindowIcon(QtGui.QIcon(LOGO_PATH))

    # displaying the UI
    credentials_dialog.exec()
    credentials_dialog.show()
