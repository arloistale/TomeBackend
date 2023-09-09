import strawberry
from datetime import datetime
from pydantic import Field, typing

@strawberry.type
class Aphorism:
    id: strawberry.ID
    title: str
    content: str
    created_at: datetime
    presented_at: typing.Optional[datetime] = Field(default_factory=datetime.now)