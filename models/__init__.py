from pydantic import BaseModel, computed_field

class User(BaseModel):
   id: int
   name: str
   email: str
   #campo opcional
   avatar: str | None = None

class Movie(BaseModel):
   id: int | None = None
   original_title: str | None = None
   genre_ids: list | None = None
   genres: list | None = None
   overview: str | None = None
   popularity: float | None = None
   poster_path: str | None = None
   title: str | None = None
   release_date: str | None = None
   vote_average: float | None = None
   vote_count: float | None = None

   @computed_field
   @property
   def poster_url(self) -> str:
      return f"https://image.tmdb.org/t/p/w185{self.poster_path}"



class Person(BaseModel):
   adult: bool | None = None
   biography: str | None = None
   birthday: str | None = None
   deathday: str | None = None
   gender: int | None = None
   homepage: str | None = None
   id: int | None = None
   imdb_id: str | None = None
   known_for_department: str | None = None
   name: str | None = None
   place_of_birth: str | None = None
   popularity: float | None = None
   profile_path: str | None = None
   known_for: list[Movie] | None = None

   @computed_field
   @property
   def profile_pic_url(self) -> str:
      return f"https://image.tmdb.org/t/p/w185{self.profile_path}"
