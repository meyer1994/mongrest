from dataclasses import dataclass

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


@dataclass
class FetchIndex:
    index: str
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class DeleteIndex(FetchIndex):
    pass


@dataclass
class CreateIndex:
    data: list[tuple]
    coll: AsyncIOMotorCollection = Depends(Collection)
