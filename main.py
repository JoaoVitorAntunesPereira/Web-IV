from fastapi import FastAPI
from tmdb.service import MovieService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
   "http://localhost",
   "http://localhost:*",
   "http://localhost:5173",
]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

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

@app.get("/person/popular/{time_window}/{page}")
def get_popular_people_by_time(time_window: str, page: int):
    movie_service = MovieService()
    
    data = movie_service.get_popular_people_by_time(time_window, page)
    
    return data

@app.get("/movies/search")
def get_movies_filter(release_year: int | None = None, popularity: str | None = None, genres: str | None = None):
    movie_service = MovieService()
    #Informar id do gênero, usar ',' para AND e '|' para OR
    data = movie_service.get_movies_filter(release_year, popularity, genres)
    return data