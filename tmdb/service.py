import json
import os
from dotenv import load_dotenv, find_dotenv
import requests
from rich import print

from models import Movie, Person

load_dotenv(find_dotenv(".env"))
TOKEN = os.environ["TMDB_TOKEN"]

def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

class MovieService:
    @staticmethod
    def get_top_rated(page=1) -> list[Movie]:
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {
            "language": "pt-BR",
            "page": page
        }

        data = get_json(url, params)
        results = data['results']
        movies = [Movie.model_validate(m) for m in results]
        return movies

    def get_movie(self, id: int) -> Movie:
        url = f"https://api.themoviedb.org/3/movie/{id}"

        params = {
            "language": "en-US"
        }

        print(url)

        data = get_json(url, params)
        movie = Movie.model_validate(data)

        return movie

    def get_person_by_id(self, id: int) -> Person:
        url = f"https://api.themoviedb.org/3/person/{id}"

        params = {
            "language": "en-US"
        }

        data = get_json(url, params)
        person = Person.model_validate(data)

        return person

    def get_person_by_name(self, name: str) -> list[Person]:
        url = f"https://api.themoviedb.org/3/search/person?query={name}"

        params = {
            "page": 1,
            "language": "en-US",
            "include_adult": "false"
        }

        data = get_json(url, params)
        results = data['results']

        people = [Person.model_validate(p) for p in results]

        return people

    def get_popular_people(self, page: int):
        url = "https://api.themoviedb.org/3/person/popular"

        params = {
            "language": "en-US",
            "page": page
        }

        data = get_json(url, params)
        results = data['results']
        people = [Person.model_validate(p) for p in results]

        return people

    def get_movies_for_person(self, name: str, page: int):
        url = f"https://api.themoviedb.org/3/search/person?query={name}"

        params = {
            "include_adult": "false",
            "language": "en-US",
            "page": page
        }

        data = get_json(url, params)
        results = data['results']
        person = Person.model_validate(results[0])

        movies = [Movie.model_validate(m) for m in person.known_for]

        return movies

    def get_popular_people_by_time(self,time_window: str, page: int):
        url = f"https://api.themoviedb.org/3/trending/person/{time_window}"

        params = {
            "language": "en-US",
            "page": page
        }

        data = get_json(url, params)
        results = data['results']
        people = [Person.model_validate(p) for p in results]
        return people

    def get_movies_filter(self, release_year: str, popularity: str, genres: str):
        url = "https://api.themoviedb.org/3/discover/movie"

        params = {
            "include_adult": "false",
            "include_video": "false",
            "language": "en-US",
            "page": 1,
            "primary_release_year": release_year,
            "sort_by": f"popularity.{popularity}",
            "with_genres": genres
        }

        data = get_json(url, params)

        return data
    
    def discover_movie(self, release_year: str, popularity: str, genres: str, title: str | None = None):
        url = "https://api.themoviedb.org/3/discover/movie"

        params = {
            "include_adult": "false",
            "include_video": "false",
            "language": "en-US",
            "page": 1,
            "primary_release_year": release_year,
            "sort_by": f"popularity.{popularity}",
            "with_genres": genres
        }

        data = get_json(url, params)
        results = data["results"]
        movies = [Movie.model_validate(m) for m in results]

        return movies
        




