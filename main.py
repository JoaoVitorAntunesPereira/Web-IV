from fastapi import FastAPI, status, Body
from tmdb.service import MovieService
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv, find_dotenv
import motor
from motor import motor_asyncio

db_url = os.environ["MONGODB_URL"] 

client = motor.motor_asyncio.AsyncIOMotorClient(db_url)
# db => objeto representa a collection pycinedb
db = client.sample_mflix

load_dotenv(find_dotenv(".env"))
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

@app.get("/trending/person/{time_window}/{page}")
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

@app.get("/mflix/users/find/")
async def list_users():
    collection = db.get_collection("users")
    results = await collection.find({}, {"_id": 0}).to_list(1000)
    print(results)
    return results

@app.get("/mflix/movies/find/")
async def list_movies():
    collection = db.get_collection("movies")
    results = await collection.find().to_list(20)
    results = [movie['title'] for movie in results]
    print(results)
    return results

@app.post("/mflix/users/save", status_code=status.HTTP_201_CREATED)
async def save_user(user: dict = Body(...)):
    collection = db.get_collection("users")

    created_user = await collection.insert_one(user)
    print("result %s" % repr(created_user.inserted_id)) 
    user_added = await collection.find_one({"_id":created_user.inserted_id}, {"_id":0})

    return user_added