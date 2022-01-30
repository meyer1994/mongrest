import json
from dataclasses import dataclass, field

from fastapi import Depends
from pydantic import conint
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


@dataclass
class Page:
    skip: conint(ge=0) = 0
    limit: conint(ge=1, le=100) = 10


@dataclass
class Query:
    query: str = field(default=r'{}')
    coll: AsyncIOMotorCollection = Depends(Collection)

    def __post_init__(self):
        self.query = json.loads(self.query)


@dataclass
class PagedQuery:
    page: Page = Depends(Page)
    query: str = field(default=r'{}')
    coll: AsyncIOMotorCollection = Depends(Collection)

    def __post_init__(self):
        self.query = json.loads(self.query)


@dataclass
class InsertOne:
    data: dict
    coll: AsyncIOMotorCollection = Depends(Collection)
