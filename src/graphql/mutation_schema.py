import strawberry

from pydantic import typing

from strawberry.types import Info

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def test(self) -> None:
        print("hello")