from dataclasses import dataclass

from bson import ObjectId
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


async def Document(_id: str) -> ObjectId:
    return ObjectId(_id)


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
class DeleteOne:
    _id: ObjectId = Depends(Document)
    coll: AsyncIOMotorCollection = Depends(Collection)
