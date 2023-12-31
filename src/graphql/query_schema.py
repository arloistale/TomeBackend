from src.graphql.aphorism_resolvers import get_aphorisms
import strawberry

from pydantic import typing

from src.graphql.aphorism import Aphorism

@strawberry.type
class Query:
    aphorisms: typing.List[Aphorism] = strawberry.field(resolver=get_aphorisms)