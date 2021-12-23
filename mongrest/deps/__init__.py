from pydantic import BaseModel
from fastapi import Depends, Request
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)

from mongrest.config import settings


class Response(BaseModel):
    data: dict


async def DB(req: Request) -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.mongo_host)
    return client[settings.mongo_db]


async def Collection(coll: str, db=Depends(DB)) -> AsyncIOMotorCollection:
    return db.get_collection(coll)
