import argparse, json, uuid
import sys
from os import path, rename

from data import static
from .api.TMDBWrapper import TMDBWrapper

def main():
    run_type, key, value = cli_parse()

    if run_type == 'preferences':
        try:
            set_preference(key, value)
        except (KeyError, FileNotFoundError) as e:
            print(e)
    
    if run_type is None:
        pass # Run GUI

    else:
        terminal_runner()


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


def load_preferences(path_to_pref):
    try:
        with open(path_to_pref, 'r') as f:
            data_json = json.load(f)            
    except FileNotFoundError as e:
        raise e(f'Problem opening file: {path_to_pref}')
    return data_json


def set_preference(key, value):
    local_json = static.PREFERENCES_JSON
    data_json = load_preferences(local_json)
    try:
        data_json[key] = value
    except KeyError as e:
        raise e(f'Key: {key} does not exist.')
    # create randomly named temporary file to avoid 
    # interference with other thread/asynchronous request
    tempfile = path.join(path.dirname(local_json), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data_json, f, indent=4)

    # rename temporary file replacing old file
    rename(tempfile, local_json)


def terminal_runner():
    try:
        user_prefs = load_preferences(static.PREFERENCES_JSON)
    except Exception as e:
        print(e)
        sys.exit(1)
    tmdbw = TMDBWrapper()
    tmdbw.api_key(user_prefs['api_key'])
    tmdbw.language(user_prefs['language'])
