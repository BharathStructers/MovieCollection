# graphqlschema/schema.py
import strawberry
from typing import List
from strawberry.types import Info
from services.movie_service import create_movie, update_movie_by_id, get_movie_by_id, get_all_movies, delete_movie_by_id,to_dict
from models.movie_schema import MovieCreateInput, MovieUpdateInput, MovieView
from config.database import get_db

@strawberry.type
class MovieType:
    id: str
    title: str
    director: str
    genre: str
    release_date: str
    description: str
    rating: int

@strawberry.type
class Query:
    @strawberry.field
    def get_movie_by_id(self, id: str, info: Info) -> MovieType:
        session = next(get_db())
        try:
            movie = get_movie_by_id(movie_id=id, session=session)
            return MovieType(**to_dict(movie))
        finally:
            session.close()

    @strawberry.field
    def get_all_movies(self, info: Info) -> List[MovieType]:
        session = next(get_db())
        try:
            movies = get_all_movies(session=session)
            return [MovieType(**to_dict(movie)) for movie in movies]
        finally:
            session.close()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_movie(self, movie_data: MovieCreateInput, info: Info) -> MovieType:
        session = next(get_db())
        try:
            movie = create_movie(movie_data=movie_data, session=session)
            return MovieType(**to_dict(movie))
        finally:
            session.close()

    @strawberry.mutation
    def update_movie(self, id: str, movie_data: MovieUpdateInput, info: Info) -> MovieType:
        session = next(get_db())
        try:
            movie = update_movie_by_id(movie_id=id, movie_data=movie_data, session=session)
            return MovieType(**to_dict(movie))
        finally:
            session.close()

    @strawberry.mutation
    def delete_movie(self, id: str, info: Info) -> str:
        session = next(get_db())
        try:
            delete_movie_by_id(movie_id=id, session=session)
            return "Movie deleted successfully"
        finally:
            session.close()

schema = strawberry.Schema(query=Query, mutation=Mutation)








# import strawberry
# from typing import List, Optional
# from config.database import get_db
# from services.movie_service import create_movie,update_movie_by_id,delete_movie_by_id,get_all_movies,get_movie_by_id

# @strawberry.type
# class MovieType:
#     id: str
#     title: str
#     director: str
#     genre: str
#     release_date: str
#     description: Optional[str] = None
#     rating: Optional[int] = None

# @strawberry.input
# class MovieCreateInput:
#     title: str
#     director: str
#     genre: str
#     release_date: str
#     description: Optional[str] = None
#     rating: Optional[int] = None

# @strawberry.input
# class MovieUpdateInput:
#     title: Optional[str] = None
#     director: Optional[str] = None
#     genre: Optional[str] = None
#     release_date: Optional[str] = None
#     description: Optional[str] = None
#     rating: Optional[int] = None

# @strawberry.type
# class Query:
#     @strawberry.field
#     def get_movie_by_id(self, id: str) -> Optional[MovieType]:
#         movie = get_movie_by_id(movie_id=id)
#         if movie:
#             return MovieType(**movie.__dict__)
#         return None

#     @strawberry.field
#     def get_all_movies(self) -> List[MovieType]:
#         movies = get_all_movies()
#         return [MovieType(**movie.__dict__) for movie in movies]

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_movie(self, movie_data: MovieCreateInput) -> MovieType:
#         movie = create_movie(movie_data=movie_data,session=get_db)
#         return MovieType(**movie.__dict__)

#     @strawberry.mutation
#     def update_movie(self, id: str, movie_data: MovieUpdateInput) -> Optional[MovieType]:
#         movie = update_movie_by_id(movie_id=id, movie_data=movie_data)
#         if movie:
#             return MovieType(**movie.__dict__)
#         return None

#     @strawberry.mutation
#     def delete_movie(self, id: str) -> str:
#         delete_movie_by_id(movie_id=id)
#         return "Movie deleted successfully"

# schema = strawberry.Schema(query=Query, mutation=Mutation)
