from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from graphqlschema.schema import schema as graphql_schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQLRouter(
    schema=graphql_schema
)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def welcome():
    return {"message": "Welcome to the Movie Collection API!"}


