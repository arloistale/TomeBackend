import strawberry
from pydantic import typing

@strawberry.type
class Aphorism:
    title: str
    content: str