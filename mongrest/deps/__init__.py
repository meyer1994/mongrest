from fastapi import Depends
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)

from mongrest.config import settings


async def DB() -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.mongo_host)
    return client[settings.mongo_db]


async def Collection(coll: str, db=Depends(DB)) -> AsyncIOMotorCollection:
    return db.get_collection(coll)
