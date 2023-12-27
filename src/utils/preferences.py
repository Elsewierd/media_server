import json
import os
from typing import Any

from .exceptions import ConfigurationError, PreferenceKeyError


class PreferencesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.preferences = self.load()

    def __str__(self, key=None) -> str:
        if key is not None:
            try:
                return f"{key}: {self.preferences[key]}"
            except KeyError:
                raise PreferenceKeyError(key)
        pref_dump = json.dumps(self.preferences, indent=4)
        return f"{self.file_path}\n{pref_dump}"

    def __getitem__(self, key: str) -> Any:
        try:
            return self.preferences[key]
        except KeyError:
            raise PreferenceKeyError(key)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str):
        if os.path.isfile(file_path) and os.path.splitext(file_path)[-1] == ".json":
            self._file_path = file_path
        else:
            raise ConfigurationError(file_path)

    def load(self):
        try:
            with open(self.file_path, "r") as f:
                data_json = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigurationError(self.file_path, f"Decoding error: {e}")
        return data_json

    def set(self, key, value, append=None):
        if value == self.preferences[key] or value in self.preferences[key]:
            return
        match append:
            case "pair":  # for creating a new key:value pair
                self.preferences[key] = value
            case "key":  # for creating a new key without a value
                self.preferences[key] = None
            case "value":  # for adding a unique value to the list paired with key
                self.preferences[key] = list(
                    set(self.preferences.get(key, [])) | {value}
                )
            case _:  # catch all for replacing the value paired with key
                if key in self.preferences:
                    self.preferences[key] = value
                else:
                    raise PreferenceKeyError(key)
        self.save()

    def save(self):
        try:
            json_obj = json.dumps(self.preferences, indent=4)
        except Exception as e:
            raise ConfigurationError(f"Error creating JSON object: {e}")
        with open(self.file_path, "w") as file:
            file.write(json_obj)
