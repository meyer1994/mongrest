import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorClient

from mongrest.config import settings


async def Collection(coll: str) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(settings.mongo_host)
    db = client[settings.mongo_db]
    return db.get_collection(coll)


JWT = OAuth2PasswordBearer(tokenUrl='http://localhost:9999/token')


async def User(token: str = Depends(JWT)) -> dict:
    alg = settings.jwt_algorithm
    sec = settings.jwt_secret
    return jwt.decode(token, key=sec, algorithms=[alg])
