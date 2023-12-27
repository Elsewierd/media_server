import os

from .exceptions import MediaFileExistsError, MediaPathError


def jellyfin_file_convention(in_path:str, name:str, *extensions:str):
    if not os.path.exists(in_path):
        raise MediaPathError(in_path)
    if os.path.isfile(in_path):
        extension = os.path.splitext(in_path)[-1]
        if not any(ext in extension for ext in extensions):
            return None
        containing_dir = os.path.dirname(in_path)
        new_dir = os.path.join(containing_dir, name)
        try:
            os.mkdir(new_dir)
        except FileExistsError:
            # Log it and check for files
            pass
        new_filepath = os.path.join(new_dir, f"{name}{extension}")
        try:
            os.rename(in_path, new_filepath)
        except FileExistsError:
            # Log it
            raise MediaFileExistsError(new_filepath)
    else:
        # If path is folder rename and rename all media files
    
