import strawberry
from typing import List, Optional
from services.movie_service import create_movie, update_movie_by_id, get_movie_by_id, get_all_movies, delete_movie_by_id

@strawberry.type
class MovieType:
    id: str
    title: str
    director: str
    genre: str
    release_date: str
    description: Optional[str] = None
    rating: Optional[int] = None

@strawberry.input
class MovieCreateInput:
    title: str
    director: str
    genre: str
    release_date: str
    description: Optional[str] = None
    rating: Optional[int] = None

@strawberry.input
class MovieUpdateInput:
    title: Optional[str] = None
    director: Optional[str] = None
    genre: Optional[str] = None
    release_date: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[int] = None

@strawberry.type
class Query:
    @strawberry.field
    def get_movie_by_id(self, id: str) -> Optional[MovieType]:
        movie = get_movie_by_id(movie_id=id)
        if movie:
            return MovieType(**movie.__dict__)
        return None

    @strawberry.field
    def get_all_movies(self) -> List[MovieType]:
        movies = get_all_movies()
        return [MovieType(**movie.__dict__) for movie in movies]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_movie(self, movie_data: MovieCreateInput) -> MovieType:
        movie = create_movie(movie_data=movie_data)
        return MovieType(**movie.__dict__)

    @strawberry.mutation
    def update_movie(self, id: str, movie_data: MovieUpdateInput) -> Optional[MovieType]:
        movie = update_movie_by_id(movie_id=id, movie_data=movie_data)
        if movie:
            return MovieType(**movie.__dict__)
        return None

    @strawberry.mutation
    def delete_movie(self, id: str) -> str:
        delete_movie_by_id(movie_id=id)
        return "Movie deleted successfully"

schema = strawberry.Schema(query=Query, mutation=Mutation)










# import strawberry
# from typing import List, Optional
# from services.movie_service import create_movie, update_movie_by_id, get_movie_by_id, get_all_movies, delete_movie_by_id

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
#         movie = create_movie(movie_data=movie_data)
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














# import typing
# import strawberry
# from c import conn
# from models.movie_model import movies
# from strawberry.types import Info

# @strawberry.type
# class Movie:
#     id: int
#     title: str
#     director: str
#     genre: str
#     release_date: str
#     description: typing.Optional[str]
#     rating: typing.Optional[int]

# @strawberry.type
# class Query:
#     @strawberry.field
#     def movie(self, id: int) -> Movie:
#         result = conn.execute(movies.select().where(movies.c.id == id)).fetchone()
#         return Movie(**result._asdict()) if result else None
    
#     @strawberry.field
#     def movies(self) -> typing.List[Movie]:
#         results = conn.execute(movies.select()).fetchall()
#         return [Movie(**row._asdict()) for row in results]

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_movie(self, title: str, director: str, genre: str, release_date: str, description: typing.Optional[str], rating: typing.Optional[int]) -> Movie:
#         movie = {
#             "title": title,
#             "director": director,
#             "genre": genre,
#             "release_date": release_date,
#             "description": description,
#             "rating": rating
#         }
#         result = conn.execute(movies.insert().values(movie))
#         movie_id = int(result.inserted_primary_key[0])
#         return Movie(id=movie_id, **movie)
    
#     @strawberry.mutation
#     def update_movie(self, id: int, title: typing.Optional[str], director: typing.Optional[str], genre: typing.Optional[str], release_date: typing.Optional[str], description: typing.Optional[str], rating: typing.Optional[int]) -> str:
#         update_data = {key: value for key, value in locals().items() if value is not None and key != 'id'}
#         result = conn.execute(movies.update().where(movies.c.id == id).values(update_data))
#         return f"{result.rowcount} Row(s) updated"
    
#     @strawberry.mutation
#     def delete_movie(self, id: int) -> bool:
#         result = conn.execute(movies.delete().where(movies.c.id == id))
#         return result.rowcount > 0









# import strawberry
# from typing import List, Optional
# from services.movie_service import create_movie, update_movie_by_id, get_movie_by_id, get_all_movies, delete_movie_by_id
# from models.movie_schema import MovieCreate, MovieUpdate

# @strawberry.type
# class MovieType:
#     id: strawberry.ID
#     title: str
#     director: str
#     genre: str
#     release_date: str
#     description: Optional[str]
#     rating: Optional[int]

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
#     def get_movie_by_id(self, id: strawberry.ID) -> Optional[MovieType]:
#         movie = get_movie_by_id(movie_id=id)
#         if movie:
#             return MovieType(
#                 id=movie.id,
#                 title=movie.title,
#                 director=movie.director,
#                 genre=movie.genre,
#                 release_date=movie.release_date,
#                 description=movie.description,
#                 rating=movie.rating
#             )
#         return None

#     @strawberry.field
#     def get_all_movies(self) -> List[MovieType]:
#         movies = get_all_movies()
#         return [
#             MovieType(
#                 id=movie.id,
#                 title=movie.title,
#                 director=movie.director,
#                 genre=movie.genre,
#                 release_date=movie.release_date,
#                 description=movie.description,
#                 rating=movie.rating
#             )
#             for movie in movies
#         ]

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_movie(self, movie_data: MovieCreateInput) -> MovieType:
#         movie = create_movie(movie_data=movie_data.dict())
#         return MovieType(
#             id=movie.id,
#             title=movie.title,
#             director=movie.director,
#             genre=movie.genre,
#             release_date=movie.release_date,
#             description=movie.description,
#             rating=movie.rating
#         )

#     @strawberry.mutation
#     def update_movie(self, id: strawberry.ID, movie_data: MovieUpdateInput) -> Optional[MovieType]:
#         movie = update_movie_by_id(movie_id=id, movie_data=movie_data.dict())
#         if movie:
#             return MovieType(
#                 id=movie.id,
#                 title=movie.title,
#                 director=movie.director,
#                 genre=movie.genre,
#                 release_date=movie.release_date,
#                 description=movie.description,
#                 rating=movie.rating
#             )
#         return None

#     @strawberry.mutation
#     def delete_movie(self, id: strawberry.ID) -> str:
#         delete_movie_by_id(movie_id=id)
#         return "Movie deleted successfully"

# schema = strawberry.Schema(query=Query, mutation=Mutation)









