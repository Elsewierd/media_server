import json
from typing import Any

from .exceptions import ConfigurationError, PreferenceKeyError

class PreferencesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.preferences = self.load_preferences()

    def __str__(self, key=None) -> str:
        if key is not None:
            try:
                return f"{key}: {self.preferences[key]}"
            except KeyError:
                raise PreferenceKeyError(key)
        pref_dump = json.dump(self.preferences, indent=4)
        return f"{self.file_path}\n{pref_dump}"

    def __getitem__(self, key: str) -> Any:
        try:
            return self.preferences[key]
        except KeyError:
            raise PreferenceKeyError(key)

    def load_preferences(self):
        try:
            with open(self.file_path, 'r') as f:
                data_json = json.load(f)
        except FileNotFoundError:
            raise ConfigurationError(self.file_path)
        return data_json

    def save_preferences(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.preferences, f)

    def set_preference(self, key, value):
        if value == self.preferences[key]:
            pass
        try:
            self.preferences[key] = value
        except KeyError:
            raise PreferenceKeyError(key)
        self.save_preferences()
