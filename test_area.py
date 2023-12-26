import os
import sys

from tmdbv3api import Movie, TMDb

from data import static
from src.utils.parser import parse_title
from src.main import load_preferences
from src.tkinter.helpers import get_directory


def main():
    preference_file = "data\preferences.json"
    user_pref = load_preferences(preference_file)

    # or

    user_pref = load_preferences("data\preferences.json")
    tm = TMDb()
    tm.api_key = user_pref["api_key"]
    tm.language = user_pref["language"]
    movie = Movie()

    folder = get_directory("Select a Folder to parse: ")

    dir_list = os.listdir(folder)

    for item in dir_list:
        item_path = os.path.join(folder, item)
        if os.path.isdir(item_path):
            title = parse_title(item)
            print(f"{item}\nTitle found: {title}")
            new_title = input("Enter alternative search title: ")
            if new_title.strip() != "":
                title = new_title
            if new_title == "s":
                continue
            results = movie.search(title)
            flag = False
            for index, item in enumerate(results):
                r_date = str(item.release_date)
                year, _, _ = r_date.split("-")
                new_dirname = f"{item.title} ({year}) [tmdbid-{item.id}]"
                print(new_dirname)
                if input("Correct? (y/No)") == "y":
                    flag = True
                    break
            if not flag:
                print("Try again.")
                sys.exit()

            new_dirname = new_dirname.translate(static.TRANSLATION_TABLE)
            updated = os.path.join(folder, new_dirname)
            os.rename(item_path, updated)
            file_list = os.listdir(updated)
            for file in file_list:
                file_path = os.path.join(updated, file)
                extension = os.path.splitext(file_path)[-1]
                if any(ext in extension for ext in static.MEDIA_EXTS):
                    title = (item.title).translate(static.TRANSLATION_TABLE)
                    new_filename = f"{title}{extension}"
                    os.rename(file_path, os.path.join(updated, new_filename))
                elif input(f"Keep {file}?").lower() != "y":
                    os.remove(file_path)


if __name__ == "__main__":
    main()
