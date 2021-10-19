import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from mongrest.config import settings


JWT = OAuth2PasswordBearer(tokenUrl='/token')


async def Collection(db: str, coll: str) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(settings.mongo_host)
    database = client[db]
    return database.get_collection(coll)


async def User(token: str = Depends(JWT)) -> dict:
    alg = settings.jwt_algorithm
    sec = settings.jwt_secret
    return jwt.decode(token, key=sec, algorithms=[alg])
