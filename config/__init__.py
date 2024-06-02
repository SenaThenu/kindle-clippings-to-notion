"""
Handles user credentials (i.e. configurations) by providing an API to save and retrieve them!
"""

from os import path
import yaml


class CredentialManager:
    def __init__(self):
        self.credentials = {"BOOK_DB_ID": "", "NOTION_TOKEN": ""}
        self._credentials_file_path = (
            "config/credentials.yaml"  # this must be in the perspective of the main.py
        )
        self._read_credentials()

    def _read_credentials(self):
        """
        Reads the credentials from the given file path
        """
        if not path.exists(self._credentials_file_path):
            self.save_credentials(book_id="", notion_token="")
        else:
            with open(self._credentials_file_path, "r") as f:
                self.credentials = yaml.full_load(f)

    def save_credentials(self, book_id: str, notion_token: str):
        """
        Saves the credentials for ease of access (locally)

        Args:
            book_id (str)
            notion_token (str)
        """
        self.credentials["BOOK_DB_ID"] = book_id
        self.credentials["NOTION_TOKEN"] = notion_token

        with open(self._credentials_file_path, "w") as f:
            yaml.dump(self.credentials, f)
