"""
Connects the GUI and the Utils
"""

import time
from os import path

from PyQt6 import QtWidgets, QtGui
from ._main_ui import Ui_mainWindow
from ._credentials_ui import Ui_Credentials

# separate thread import for multi-threading
from ._worker_thread import WorkerThread


class MainWindow:
    def __init__(self):
        """
        IMPORTANT: To create the MainWindow call the config() method after initialising this class!
        """
        # window specifications
        self._logo_path = path.abspath(
            path.join(
                path.dirname(path.dirname(__file__)), "readme_assets/app_logo.png"
            )
        )

        # importing pre-built interfaces
        self.main_gui = Ui_mainWindow()
        self.credentials_gui = Ui_Credentials()

        # default stylesheets
        self._error_style = "color: red;\nfont-weight: bold;"
        self._success_style = "color: green;\nfont-weight: bold;"

    def config(
        self, config_manager: object, extract_and_upload_clippings: object
    ) -> object:
        """
        Returns the GUI after binding all the functions to it!

        Args:
            config_manager (object)
            extract_and_upload_clippings (object): callback used to extract and upload clippings

        Returns:
            object: the functional gui object
        """
        self.config_manager = config_manager
        self.extract_and_upload_clippings = extract_and_upload_clippings

        # binding the qt-generated UI
        main_window = QtWidgets.QMainWindow()
        self.main_gui.setupUi(main_window)

        # sets up UI elements
        self._setup_menubar()
        self._enable_browse_path()
        self.main_gui.credentialsBtn.clicked.connect(self._configure_credentials_editor)
        self.main_gui.syncBtn.clicked.connect(self._execute_syncing)

        # hiding some stuff until sync is pressed
        self.main_gui.syncProgressBar.setHidden(True)
        self.main_gui.syncStatusMessage.setHidden(True)

        # basic main window configurations
        main_window.setWindowIcon(QtGui.QIcon(self._logo_path))

        return main_window

    def _enable_browse_path(self):
        """
        Allows the user ot select the path they need
        """

        def _browse_path():
            # options = QtWidgets.QFileDialog.DontUseNativeDialog
            path = QtWidgets.QFileDialog.getOpenFileName(
                self.main_gui.centralwidget,
                "Open Your Kindle Clippings Text File",
                directory=self.config_manager.config["SELECTED_PATH"],
                filter="*.txt",
            )

            if path[0]:
                self.main_gui.pathInput.setText(path[0])
                self.config_manager.save_path(path[0])

        self.main_gui.pathInput.setText(self.config_manager.config["SELECTED_PATH"])
        self.main_gui.browsePath.clicked.connect(_browse_path)

    def _finished_syncing_changes(self, message_type: str):
        """
        Updates the GUI to indicate completion!

        Args:
            message_type (str): either success or error
        """
        if message_type == "success":
            _btn_text = "Sync!"
        else:
            _btn_text = "Try Again!"

        self.main_gui.syncBtn.setEnabled(True)
        self.main_gui.syncBtn.setText(_btn_text)
        self.main_gui.syncProgressBar.setHidden(True)

    def _display_success_message(self):
        """
        Displays "Synced Successfully!"
        """
        self.main_gui.syncStatusMessage.setStyleSheet(self._success_style)

        # a quick pause to make sure this happens after all the update GUI signals executed
        time.sleep(1)
        self.main_gui.syncStatusMessage.setText("Synced Successfully! 👍")

        self._finished_syncing_changes("success")

    def _display_error_message(self, message: str):
        """
        Displays the given error message

        Args:
            message (str)
        """
        self.main_gui.syncStatusMessage.setStyleSheet(self._error_style)

        # a quick pause to make sure this happens after all the update GUI signals executed
        time.sleep(1)
        self.main_gui.syncStatusMessage.setText(message)

        self._finished_syncing_changes("error")

    def _execute_syncing(self):
        # ui changes to respond to the user command
        self.main_gui.syncBtn.setEnabled(False)
        self.main_gui.syncBtn.setText("Syncing...")
        self.main_gui.syncStatusMessage.setHidden(False)
        self.main_gui.syncStatusMessage.setStyleSheet("")
        self.main_gui.syncProgressBar.setHidden(False)

        # setting up the worker thread and executing the action in a separate
        self.worker_thread = WorkerThread(
            self.extract_and_upload_clippings,
            {
                "config_manager": self.config_manager,
                "display_error_message": self._display_error_message,
            },
            self._display_success_message,
        )

        self.worker_thread.progress.connect(self._update_progress_bar)
        self.worker_thread.status_message.connect(self._update_sync_status)

        self.worker_thread.start()

    def _setup_menubar(self):
        """
        Makes the menu bar of the main window functional
        """
        self.main_gui.actionCredentials.triggered.connect(
            self._configure_credentials_editor
        )

    def _set_up_credentials_editor_functions(self):
        """
        Makes the UI elements in the credentials editor functional
        """
        # storing references to the 2 input objects
        database_id_input = self.credentials_gui.databaseIdInput
        notion_token_input = self.credentials_gui.notionAuthTokenInput

        # showing the current values
        database_id_input.setText(self.config_manager.config["BOOK_DB_ID"])
        notion_token_input.setText(self.config_manager.config["NOTION_TOKEN"])

        # hiding some stuff
        self.credentials_gui.savedMessageLabel.setHidden(True)

        # enabling the saving button
        def _save_credentials():
            # saving in progress depiction
            self.credentials_gui.saveBtn.setText("Saving...")
            self.credentials_gui.saveBtn.setEnabled(False)
            self.credentials_gui.savedMessageLabel.setHidden(True)

            self.config_manager.save_credentials(
                book_id=database_id_input.text(),
                notion_token=notion_token_input.text(),
            )

            # showing the success message
            self.credentials_gui.savedMessageLabel.setStyleSheet(self._success_style)
            self.credentials_gui.savedMessageLabel.setHidden(False)

            # bringing the save button back to normal
            self.credentials_gui.saveBtn.setText("Save")
            self.credentials_gui.saveBtn.setEnabled(True)

        self.credentials_gui.saveBtn.clicked.connect(_save_credentials)

    def _configure_credentials_editor(self):
        """
        Creates the interface for the users to edit their credentials
        """
        # binding the qt-generated UI
        credentials_dialog = QtWidgets.QDialog()
        self.credentials_gui.setupUi(credentials_dialog)

        # configuring the UI
        credentials_dialog.setWindowTitle("Hashtags Editor")
        credentials_dialog.setWindowIcon(QtGui.QIcon(self._logo_path))
        self._set_up_credentials_editor_functions()

        # displaying the UI
        credentials_dialog.exec()
        credentials_dialog.show()

    def _update_progress_bar(self, value):
        self.main_gui.syncProgressBar.setValue(value)

    def _update_sync_status(self, message):
        self.main_gui.syncStatusMessage.setText(message)
