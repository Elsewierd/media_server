from tmdbv3api import TV, Movie, TMDb

API_KEY = "a3a7bab86fcaab64c6a13deccc2c5134"


class TMDBWrapper:
    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        tmdb = TMDb()
        tmdb.api_key = API_KEY
        tmdb.language = "en"
        self.movie()
        self.series()

    @property
    def movie(self):
        self._movie = Movie()
        return self._movie

    @property
    def series(self):
        self._series = TV()
        return self._series

    def search(self, media_type, query):
        try:
            property_instance = getattr(self, media_type)
        except AttributeError("Attribute {media_type} does not exist") as e:
            raise e
        results = property_instance.search(query)
        # Process the search results as needed
        return results
    
    def


# TODO: Add properties for seasons, episodes, and a details method
