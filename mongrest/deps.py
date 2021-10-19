from dataclasses import dataclass

from bson import ObjectId
from pydantic import conint
from fastapi import Depends, Request
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from mongrest.config import settings


async def Collection(coll: str) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(settings.mongo_host)
    db = client[settings.mongo_db]
    return db.get_collection(coll)


async def Document(_id: str) -> ObjectId:
    return ObjectId(_id)


async def Params(req: Request) -> dict:
    params = dict(req.query_params)
    params.pop('_page', None)
    params.pop('_size', None)
    return params


@dataclass
class InsertOne:
    data: dict
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class UpdateOne:
    data: dict
    _id: ObjectId = Depends(Document)
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class FetchOne:
    _id: ObjectId = Depends(Document)
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class DeleteOne(FetchOne):
    pass


@dataclass
class Page:
    _page: conint(ge=1) = 1
    _size: conint(ge=1) = 10

    @property
    def _skip(self) -> int:
        return (self._page - 1) * self._size


@dataclass
class Query:
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class PagedQuery:
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)
    page: Page = Depends(Page)


@dataclass
class AggregateQuery:
    data: list[dict]
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)
    page: Page = Depends(Page)


@dataclass
class FetchIndex:
    index: str
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class DeleteIndex(FetchIndex):
    pass


@dataclass
class CreateIndex:
    data: list[tuple]
    coll: AsyncIOMotorCollection = Depends(Collection)
