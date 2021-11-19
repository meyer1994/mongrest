from dataclasses import dataclass

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


@dataclass
class FetchIndex:
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class DeleteIndex:
    index: str
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class CreateIndex:
    data: list[tuple]
    coll: AsyncIOMotorCollection = Depends(Collection)
