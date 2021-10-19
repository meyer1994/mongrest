from dataclasses import dataclass

from fastapi import Depends, Request
from pydantic import conint
from motor.motor_asyncio import AsyncIOMotorCollection

from . import Collection


async def Params(req: Request) -> dict:
    params = dict(req.query_params)
    params.pop('_page', None)
    params.pop('_size', None)
    return params


@dataclass
class Page:
    _page: conint(ge=1) = 1
    _size: conint(ge=1) = 10

    @property
    def _skip(self) -> int:
        return (self._page - 1) * self._size


@dataclass
class Query:
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)


@dataclass
class PagedQuery:
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)
    page: Page = Depends(Page)


@dataclass
class AggregateQuery:
    data: list[dict]
    query: dict = Depends(Params)
    coll: AsyncIOMotorCollection = Depends(Collection)
    page: Page = Depends(Page)
