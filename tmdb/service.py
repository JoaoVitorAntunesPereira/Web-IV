import os
from dotenv import load_dotenv, find_dotenv
import requests
from rich import print

from models import Movie

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
    def get_top_rated(page=1):
        url = "https://api.themoviedb.org/3/movie/top_rated"
        params = {
            "language": "pt-BR",
            "page": page
        }

        data = get_json(url, params)
        results = data['results']
        movies = [Movie.model_validate(m) for m in results]
        return movies

    def get_movie(self, id: int):
        url = "https://api.themoviedb.org/3/movie/"
        url = url+id

        params = {
            "language": "en-US"
        }

        print(url)

        data = get_json(url, params)
        return data
