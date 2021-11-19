import jwt
from pydantic import BaseModel
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)

from mongrest.config import settings


JWT = OAuth2PasswordBearer(tokenUrl='/token')


class Response(BaseModel):
    data: dict


async def DB(req: Request) -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.mongo_host)
    return client[settings.mongo_db]


async def Collection(coll: str, db=Depends(DB)) -> AsyncIOMotorCollection:
    return db.get_collection(coll)


async def User(token: str = Depends(JWT)) -> dict:
    alg = settings.jwt_algorithm
    sec = settings.jwt_secret
    return jwt.decode(token, key=sec, algorithms=[alg])
