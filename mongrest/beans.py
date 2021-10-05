import functools

from motor.motor_asyncio import AsyncIOMotorClient

from mongrest.config import settings


@functools.cache
def get_db():
    db = AsyncIOMotorClient(settings.mongo_host)
    return db[settings.mongo_db]
