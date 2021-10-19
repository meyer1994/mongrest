import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)

from mongrest.config import settings


JWT = OAuth2PasswordBearer(tokenUrl='/token')


async def DB(db: str) -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.mongo_host)
    return client[db]


async def Collection(coll: str, db=Depends(DB)) -> AsyncIOMotorCollection:
    return db.get_collection(coll)


async def User(token: str = Depends(JWT)) -> dict:
    alg = settings.jwt_algorithm
    sec = settings.jwt_secret
    return jwt.decode(token, key=sec, algorithms=[alg])
