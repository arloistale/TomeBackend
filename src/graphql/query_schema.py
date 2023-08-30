import strawberry

from pydantic import typing

from src.graphql.aphorism import Aphorism

def get_aphorisms():
    return [
        Aphorism(
            title="The Great Gatsby",
            content="F. Scott Fitzgerald",
        ),
    ]

@strawberry.type
class Query:
    aphorisms: typing.List[Aphorism] = strawberry.field(resolver=get_aphorisms)