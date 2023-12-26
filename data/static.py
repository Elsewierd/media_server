PREFERENCES_JSON = "data/preferences.json"
MEDIA_EXTS = ["avi", "mkv", "m4v", "mp4"]
INVALID_CHARS = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
TRANSLATION_TABLE = str.maketrans("", "", "".join(INVALID_CHARS))