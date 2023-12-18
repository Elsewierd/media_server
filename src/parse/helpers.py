import re

from .Exceptions import PatternError

def parse_title(file_name):
    pattern = r"^([\w\d: _]*)[\W\D\.]?"
    match_item = re.search(pattern, file_name)
    if match_item is None:
        raise PatternError(f"Title pattern not found in {file_name}")
    return match_item.group(1)

def parse_episode(filename):
    pattern = r"([S|s](?P<season>\d*)[E|e].?(?P<episode>\d*))|[E|e].?(?P<no_season>\d*)"
    match_item = re.search(pattern, filename)
    if match_item is None:
        raise TypeError("Did not match pattern")
    if match_item.group("no_season"):
        return (1, int(match_item.group("no_season")))
    return (int(match_item.group("season")), int(match_item.group("episode")))