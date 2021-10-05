from bson import ObjectId
from starlette.requests import Request
from motor.motor_asyncio import AsyncIOMotorCollection

from mongrest import beans


async def collection(coll: str) -> AsyncIOMotorCollection:
    return beans.get_db().get_collection(coll)


async def filter(req: Request) -> dict:
    return dict(req.query_params)


async def objid(_id: str) -> ObjectId:
    return ObjectId(_id)


async def removeid(data: dict) -> dict:
    data.pop('_id', None)
    return data
