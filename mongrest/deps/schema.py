from dataclasses import dataclass

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from . import DB


@dataclass
class FetchSchema:
    coll: str
    db: AsyncIOMotorDatabase = Depends(DB)


@dataclass
class DeleteSchema:
    coll: str
    db: AsyncIOMotorDatabase = Depends(DB)


@dataclass
class CreateSchema:
    coll: str
    schema: dict
    db: AsyncIOMotorDatabase = Depends(DB)
