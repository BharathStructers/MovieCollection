import uuid
from sqlalchemy.orm import Session
from models.movie_model import Movie
from models.movie_schema import MovieCreateInput, MovieUpdateInput

def create_movie(movie_data: MovieCreateInput, session: Session) -> Movie:
    id_data = str(uuid.uuid4())
    movie = Movie(id=id_data,
            title=movie_data.title,
            director=movie_data.director,
            genre=movie_data.genre,
            release_date=movie_data.release_date,
            description=movie_data.description,
            rating=movie_data.rating)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

def update_movie_by_id(movie_id: str, movie_data: MovieUpdateInput, session: Session) -> Movie:
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        for key, value in movie_data.__dict__.items():
            if value is not None:
                setattr(movie, key, value)
        session.commit()
        session.refresh(movie)
    return movie

def get_movie_by_id(movie_id: str, session: Session) -> Movie:
    return session.query(Movie).filter(Movie.id == movie_id).first()

def get_all_movies(session: Session) -> list[Movie]:
    return session.query(Movie).all()

def delete_movie_by_id(movie_id: str, session: Session):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()



def to_dict(instance):
    """Convert SQLAlchemy model instance to dictionary excluding internal state."""
    return {column.name: getattr(instance, column.name) for column in instance.__table__.columns}






# from sqlalchemy.orm import Session
# from models.movie_model import Movie
# from models.movie_schema import MovieCreateInput, MovieUpdateInput

# def create_movie(db: Session, movie_data: MovieCreateInput):
#     db_movie = Movie(**movie_data.dict())
#     db.add(db_movie)
#     db.commit()
#     db.refresh(db_movie)
#     return db_movie

# def update_movie_by_id(db: Session, movie_id: str, movie_data: MovieUpdateInput):
#     db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if not db_movie:
#         return None
#     for key, value in movie_data.dict(exclude_unset=True).items():
#         setattr(db_movie, key, value)
#     db.commit()
#     db.refresh(db_movie)
#     return db_movie

# def get_movie_by_id(db: Session, movie_id: str):
#     return db.query(Movie).filter(Movie.id == movie_id).first()

# def get_all_movies(db: Session):
#     return db.query(Movie).all()

# def delete_movie_by_id(db: Session, movie_id: str):
#     db_movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if db_movie:
#         db.delete(db_movie)
#         db.commit()











# from sqlalchemy.orm import Session
# from models.movie_model import Movie
# from models.movie_schema import MovieCreateInput, MovieUpdateInput
# from fastapi import HTTPException
# import uuid

# def create_movie(moviedata: MovieCreateInput, session: Session):
#     id_data = str(uuid.uuid4())
#     try:
#         movie = Movie(
#             id=id_data,
#             title=moviedata.title,
#             director=moviedata.director,
#             genre=moviedata.genre,
#             release_date=moviedata.release_date,
#             description=moviedata.description,
#             rating=moviedata.rating
#         )
#         session.add(movie)
#         session.commit()
#         session.refresh(movie)
#         return movie
#     except Exception as e:
#         session.rollback()
#         raise HTTPException(status_code=400, detail=str(e))

# def update_movie_by_id(movie_id: str, moviedata: MovieUpdateInput, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")

#     movie.title = moviedata.title
#     movie.director = moviedata.director
#     movie.genre = moviedata.genre
#     movie.release_date = moviedata.release_date
#     movie.description = moviedata.description
#     movie.rating = moviedata.rating
#     session.commit()
#     session.refresh(movie)
#     return movie

# def get_movie_by_id(movie_id: str, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# def get_all_movies(session: Session):
#     return session.query(Movie).all()

# def delete_movie_by_id(movie_id: str, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     session.delete(movie)
#     session.commit()
#     return {"message": "Movie deleted successfully"}













# import uuid
# from fastapi import HTTPException
# import strawberry
# from typing import Optional,List
# from sqlalchemy.orm import Session
# from models.movie_model import Movie
# from models.movie_schema import MovieBase,MovieCreate,MovieUpdate,MovieView


# def create_movie(moviedata: MovieCreate, session: Session):
#   id_data = str(uuid.uuid4())
#   try:
#       movie = Movie(
#           id=id_data,
#           title=moviedata.title,
#           director=moviedata.director,
#           genre=moviedata.genre,
#           release_date=moviedata.release_date,
#           description=moviedata.description,
#           rating=moviedata.rating
#       )
#       session.add(movie)
#       session.commit()
#       session.refresh(movie)
#       return movie
#   except Exception as e:
#       session.rollback()
#       raise HTTPException(status_code=400, detail=str(e))

# def update_movie_by_id(movie_id: str, moviedata: MovieUpdate, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")

#     movie.title = moviedata.title
#     movie.director = moviedata.director
#     movie.genre = moviedata.genre
#     movie.release_date = moviedata.release_date
#     movie.description = moviedata.description
#     movie.rating = moviedata.rating
#     session.commit()
#     session.refresh(movie)
#     return movie

# def get_movie_by_id(movie_id: str, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# def get_all_movies(session: Session):
#     return session.query(Movie).all()

# def delete_movie_by_id(movie_id: str, session: Session):
#     movie = session.query(Movie).filter(Movie.id == movie_id).first()
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     session.delete(movie)
#     session.commit()
#     return {"message": "Movie deleted successfully"}