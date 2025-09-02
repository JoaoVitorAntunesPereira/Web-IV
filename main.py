    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/movies/top/{page}")
    def get_top_ranked_movies(page = 1):
        from tmdb.service import MovieService

        movies = MovieService.get_top_rated(page)

        return movies

    @app.get("/movies/movie/{id}")
    def get_movie_by_id(id):
        from tmdb.service import MovieService

        movie_service = MovieService()

        movie = movie_service.get_movie(id)
        return movie

