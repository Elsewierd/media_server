from tmdbv3api import TV, Movie, TMDb

API_KEY = "a3a7bab86fcaab64c6a13deccc2c5134"


class TMDBWrapper():
    def __init__(self) -> None:
        self._tmdb = TMDb()
        self._api_key = None
        self._language = None
        self._movie = None
        self._series = None

    @property
    def api_key(self, api_key):
        self._api_key = api_key
        if self._tmdb is not None:
            self._tmdb.api_key = self._api_key
        return self._api_key

    @property
    def language(self, language):
        self._language = language
        if self._tmdb is not None:
            self._tmdb.language = self._language
        return self._language

    def movie(self):
        if self._movie is None:
            self._movie = Movie()
        return self._movie

    def series(self):
        if self._series is None:
            self._series = TV()
        return self._series

    def search(self, media_type, query):
        try:
            property_instance = getattr(self, media_type)
        except AttributeError("Attribute {media_type} does not exist") as e:
            print(f'Error: {e}')
            return None
        
        if property_instance is None:
            property_instance = property_instance()

        return property_instance.search(query)

    def details(self, media_type, id, *args):
        detail_dict = {}
        try:
            property_instance = getattr(self, media_type)
        except AttributeError(f"Attribute {media_type} does not exist") as e:
            print(f'Error: {e}')
            return None
        output = property_instance.details(id)
        for arg in args:
            try:
                value_instance = getattr(output, arg)
            except AttributeError(f"ID: {id} does not have an attribute: {arg}") as e:
                print(f'Error: {e}')
            else:
                detail_dict[arg] = value_instance
        return detail_dict


# TODO: Add properties for seasons, episodes, and a details method
def media(func):
    def wrapper():
        func()
    return wrapper