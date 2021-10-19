from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from mongrest.config import settings


async def Collection(coll: str) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(settings.mongo_host)
    db = client[settings.mongo_db]
    return db.get_collection(coll)
