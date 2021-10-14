from dataclasses import dataclass

from bson import ObjectId
from fastapi import Depends
from pydantic import conint
from starlette.requests import Request
from motor.motor_asyncio import AsyncIOMotorCollection

from mongrest import beans


async def Collection(coll: str) -> AsyncIOMotorCollection:
    return beans.get_db().get_collection(coll)


async def Parameters(req: Request) -> dict:
    params = dict(req.query_params)
    params.pop('page', None)
    params.pop('size', None)
    return params


Coll = Depends(Collection)
Params = Depends(Parameters)


@Depends
@dataclass
class Page:
    page: conint(ge=1) = 1
    size: conint(ge=1) = 10

    @property
    def skip(self) -> int:
        return (self.page - 1) * self.size


@Depends
@dataclass
class Filter:
    coll: AsyncIOMotorCollection = Depends(Collection)
    filter: dict = Depends(Parameters)


@Depends
@dataclass
class Doc:
    coll: AsyncIOMotorCollection = Depends(Collection)
    _id: ObjectId = Depends(ObjectId)
