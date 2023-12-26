import argparse
import re

from .exceptions import PatternError

def cli_parse():
    parser = argparse.ArgumentParser(description='Media File Utility')

    # Add command line arguments
    parser.add_argument('-d', '--debug', action='store_true', help='Run in debug mode (no GUI)')
    parser.add_argument('-p', '--preferences', nargs=2, metavar=('key', 'value'), help='Adjust preferences')
    
    args = parser.parse_args()

    if args.debug:
        print('Running in debug mode (no GUI)')
        return 'debug', None, None

    if args.preferences:
        key, value = args.preferences
        print(f'Adjusting preferences: {key} = {value}')
        return 'preference', key, value
    
    return None, None, None

def parse_title(file_name):
    pattern = r"^([\w\d: _,]*)[\W\D\.]?"
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