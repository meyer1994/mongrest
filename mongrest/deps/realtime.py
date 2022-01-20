import json
from dataclasses import dataclass, field

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


@dataclass
class Query:
    query: str = field(default=r'{}')
    coll: AsyncIOMotorCollection = Depends(Collection)

    def __post_init__(self):
        self.query = json.loads(self.query)
