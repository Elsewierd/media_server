
from tmdbv3api import TV, Movie, TMDb, Season, Episode

class TMDBManager:
    def __init__(self, api_key=None, language=None):
        self._tmdb = TMDb()
        self.api_key = api_key
        self.language = language
        self._movie = Movie()
        self._series = TV()
        self._season = Season()
        self._episode = Episode()

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
        if self._tmdb is not None:
            self._tmdb.api_key = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value
        if self._tmdb is not None:
            self._tmdb.language = value

    @property
    def movie(self):
        return self._movie

    @property
    def series(self):
        return self._series

    @property
    def season(self):
        return self._season

    @property
    def episode(self):
        return self._episode

    def search(self, media_type:str, query:str):
        try:
            property_instance = getattr(self, media_type.lower())
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
        if args is None:
            return output
        for arg in args:
            try:
                value_instance = getattr(output, arg)
            except AttributeError(f"ID: {id} does not have an attribute: {arg}") as e:
                print(f'Error: {e}')
            else:
                detail_dict[arg] = value_instance
        return detail_dict
