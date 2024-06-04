"""
Handles user config (i.e. configurations) by providing an API to save and retrieve them!
"""

from os import path
import yaml


class ConfigManager:
    def __init__(self):
        self.config = {
            "BOOK_DB_ID": "",
            "NOTION_TOKEN": "",
            "SELECTED_PATH": "",
        }
        self._config_file_path = (
            "config/config.yaml"  # this must be in the perspective of the main.py
        )
        self._read_config()

    def _read_config(self):
        """
        Reads the config from the given file path
        """
        if not path.exists(self._config_file_path):
            # creates a new file with empty data
            self._write_to_config_file()
        else:
            with open(self._config_file_path, "r") as f:
                # making sure the file is not empty!
                config_file_data = yaml.full_load(f)
                if config_file_data:
                    # updating a configs dynamically
                    for key, value in config_file_data.items():
                        if value != None:
                            self.config[key] = value
                else:
                    self._write_to_config_file()

    def _write_to_config_file(self):
        """
        Writes the data to config.yaml
        """
        with open(self._config_file_path, "w") as f:
            yaml.dump(self.config, f)

    def save_credentials(self, book_id: str, notion_token: str):
        """
        Saves the credentials for ease of access (locally)

        Args:
            book_id (str)
            notion_token (str)
        """
        self.config["BOOK_DB_ID"] = book_id
        self.config["NOTION_TOKEN"] = notion_token

        self._write_to_config_file()

    def save_path(self, current_path: str):
        """
        Saves the path the user has currently selected as the path to minimise redundancy the next time the user opens the application!

        Args:
            current_path (str)
        """
        self.config["SELECTED_PATH"] = current_path
        self._write_to_config_file()
