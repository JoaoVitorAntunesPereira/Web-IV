from fastapi import FastAPI
from tmdb.service import MovieService

app = FastAPI()

@app.get("/movies/top/{page}")
def get_top_ranked_movies(page = 1):

    movies = MovieService.get_top_rated(page)

    return movies

@app.get("/movies/movie/{id}")
def get_movie_by_id(id):

    movie_service = MovieService()

    movie = movie_service.get_movie(id)
    return movie

@app.get("/person/{id}")
def get_person_by_id(id: int):
    movie_service = MovieService()

    person = movie_service.get_person_by_id(id)

    return person

@app.get("/person/name/{name}")
def get_person_by_name(name: str):
    data = MovieService().get_person_by_name(name)

    return data

@app.get("/person/popular/{page}")
def get_popular_people(page: int | None = None):
    movie_service = MovieService()

    data = movie_service.get_popular_people(page)
    return data

@app.get("/person/movies/{name}/{page}")
def get_movies_for_person(name: str, page: int | None = None):
    movie_service = MovieService()

    data = movie_service.get_movies_for_person(name, page)

    return data
