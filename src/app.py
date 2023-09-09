import strawberry

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from src.graphql.mutation_schema import Mutation
from src.graphql.query_schema import Query

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))

def create_app():
    app = FastAPI()
    
    graphql_app = GraphQLRouter(
        schema,
        graphiql=True
    )
    app.include_router(graphql_app, prefix="/graphql")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app