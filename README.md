26DEC2023
    Renamed runner.py to main.py
    Renamed TMDBWrapper.py to moviedb.py
    Moved parser.py and exceptions.py to src/utils/
    Created preferences.py
        File contains class PreferenceManager to hold and manipulate the user's preferences
    exceptions.py
        contains the custom exceptions for this app. All exceptions are a subclass of
        class MediaFileUtilityError(Exception)
    test_area.py
        File used to test and build functions prior to migrating them to the proper folder will not be included in release