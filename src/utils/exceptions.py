class MediaFileUtilityError(Exception):
    
    @property
    def message(self):
        return "--Error Occured--"

class ConfigurationError(MediaFileUtilityError):
    def __init__(self, file_path, message="Configuration Error") -> None:
        self._file_path = file_path
        super().__init__(message)
    
    @property
    def message(self):
        return f"{super().message}: {self._file_path}"
    
class PreferenceKeyError(MediaFileUtilityError):
    def __init__(self, key, message="Key Error") -> None:
        self._key = key
        super().__init__(message)

    @property
    def message(self):
        return f"{super().message}: {self._key}"
    
class MediaTypeError(MediaFileUtilityError):
    def __init__(self, media_type, message="Media Type Error") -> None:
        self._media_type=media_type
        super().__init__(message)

    @property
    def message(self):
        return f"{super().message}: {self._media_type}"
    
class MediaFileExistsError(MediaFileUtilityError):
    def __init__(self, filename, message="File Already Exists") -> None:
        self._filename=filename
        super().__init__(message)

    @property
    def message(self):
        return f"{super().message}: {self._filename}"

class MediaPathError(MediaFileUtilityError):
    def __init__(self, error_path, message="Path is Invalid") -> None:
        self._error_path=error_path
        super().__init__(message)

    @property
    def message(self):
        return f"{super().message}: {self._error_path}"