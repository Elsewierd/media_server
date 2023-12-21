import argparse, json, uuid
from os import path, rename

from api.TMDBWrapper import TMDBWrapper

def main():
    run_type, key, value = cli_parse()

    if run_type == 'preferences':
        try:
            set_preference(key, value)
        except (KeyError, FileNotFoundError) as e:
            print(e)



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

def set_preference(key, value):
    preferences_json = './data/preferences.json'
    try:
        with open(preferences_json, 'r') as f:
            data = json.load(f)
            try:
                data[key] = value
            except KeyError as e:
                raise e(f'Key: {key} does not exist.')
    except FileNotFoundError as e:
        raise e(f'Problem opening file: {preferences_json}')
    # create randomly named temporary file to avoid 
    # interference with other thread/asynchronous request
    tempfile = path.join(path.dirname(preferences_json ), str(uuid.uuid4()))
    with open(tempfile, 'w') as f:
        json.dump(data, f, indent=4)

    # rename temporary file replacing old file
    rename(tempfile, preferences_json)
