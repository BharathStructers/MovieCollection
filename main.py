from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from GraphQL.schema import schema as graphql_schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQLRouter(graphql_schema))


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from strawberry.fastapi import GraphQLRouter
# from GraphQL.schema import schema as graphql_schema

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.add_route("/graphql", GraphQLRouter(graphql_schema))

# @app.get("/")
# def welcome():
#     return {"message": "Welcome to the Movie Collection API"}



# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from strawberry.fastapi import GraphQLRouter
# from GraphQL.schema import schema as graphql_schema
# from config.database import get_db, SessionLocal

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # GraphQL route
# app.add_route("/g", GraphQLRouter(graphql_schema))

# @app.get("/")
# def welcome():
#     return {"welcome"}

