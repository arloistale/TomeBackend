import strawberry

from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from src.graphql.mutation_schema import Mutation
from src.graphql.query_schema import Query

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True))

def create_app():
    app = FastAPI()
    graphql_app = GraphQLRouter(schema)
    app.include_router(graphql_app, prefix="/graphql")

    return app