from typing import Optional
import strawberry

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




















from pydantic import BaseModel
# from datetime import datetime
# from typing import Optional



# class MovieCreateInput(BaseModel):
#     title: str
#     director: str
#     genre: str
#     release_date: str
#     description: Optional[str] = None
#     rating: Optional[int] = None

# class MovieUpdateInput(BaseModel):
#     title: Optional[str] = None
#     director: Optional[str] = None
#     genre: Optional[str] = None
#     release_date: Optional[str] = None
#     description: Optional[str] = None
#     rating: Optional[int] = None

class MovieView(BaseModel):
    id: str
    title: str
    director: str
    genre: str
    release_date: str
    description: Optional[str] = None
    rating: Optional[int] = None






# class MovieBase(BaseModel):
#   title: str
#   director: str
#   genre: str
#   release_date: datetime
#   description: Optional[str] = None
#   rating: Optional[int] = None

# class MovieCreate(BaseModel):
#   title:str
#   director:str
#   genre:str
#   release_date:Optional[datetime]=None
#   description: Optional[str] = None
#   rating: Optional[int] = None


# # class MovieUpdate(MovieBase):
# #   title:str
# #   director:str
# #   genre:str
# #   release_date: Optional[datetime]=None
# #   description: Optional[str] = None
# #   rating: Optional[int] = None


# class MovieView(MovieBase):
#   id:str
#   title:str
#   director:str
#   genre:str
#   release_date: datetime
#   description: Optional[str] = None
#   rating: Optional[int] = None
