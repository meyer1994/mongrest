import json
from dataclasses import dataclass, field

from fastapi import Depends
from pydantic import conint
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


@dataclass
class Page:
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10
    skip: int = field(init=False)

    def __post_init__(self):
        self.skip = (self.page - 1) * self.size


@dataclass
class Query:
    query: str = field(default=r'{}')
    coll: AsyncIOMotorCollection = Depends(Collection)

    def __post_init__(self):
        self.query = json.loads(self.query)


@dataclass
class PagedQuery(Query):
    page: Page = Depends(Page)
