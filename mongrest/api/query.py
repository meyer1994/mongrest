from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from mongrest import deps


router = APIRouter()


@router.get('/{coll}/_find')
async def find(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter)
) -> list:
    cursor = coll.find(filtr)
    return await cursor.to_list(10)


@router.delete('/{coll}/_find')
async def delete(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter)
) -> list:
    result = await coll.delete_many(filtr)
    return result.raw_result


@router.get('/{coll}/_findone')
async def findone(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter)
) -> dict:
    return await coll.find_one(filtr)


@router.delete('/{coll}/_findone')
async def deleteone(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter)
) -> dict:
    return await coll.find_one_and_delete(filtr)


@router.post('/{coll}/_aggregate')
async def aggregate(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter),
    data: list = []
) -> list:
    aggreg = [{'$match': filtr}, *data]
    cursor = coll.aggregate(aggreg)
    return await cursor.to_list(10)


@router.get('/{coll}/_count')
async def count(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    filtr: dict = Depends(deps.filter)
) -> list:
    return await coll.count_documents(filtr)
