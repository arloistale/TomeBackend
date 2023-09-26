from src.graphql.aphorism import Aphorism
from src.graphql.aphorism_resolvers import present_random_aphorism
import strawberry

from typing import Annotated, Union

@strawberry.type
class PresentRandomAphorismSuccess:
    aphorism: Aphorism

@strawberry.type 
class AphorismAlreadyPresentedError:
    message: str

Response = Annotated[
    Union[PresentRandomAphorismSuccess, AphorismAlreadyPresentedError], 
    strawberry.union("PresentRandomAphorismResponse"),
]

@strawberry.type
class Mutation:

    @strawberry.mutation
    def present_random_aphorism(self) -> Response:

        aphorism, error = present_random_aphorism()

        if error is not None:
            return AphorismAlreadyPresentedError(message=error)

        return PresentRandomAphorismSuccess(aphorism=aphorism)
