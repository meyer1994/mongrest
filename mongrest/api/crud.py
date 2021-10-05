from bson import ObjectId
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorCollection

from mongrest import deps


router = APIRouter()


@router.get('/{coll}/{_id}')
async def get(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    _id: ObjectId = Depends(deps.objid)
) -> dict:
    return await coll.find_one({'_id': _id})


@router.put('/{coll}/{_id}')
async def put(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    _id: ObjectId = Depends(deps.objid),
    data: dict = Depends(deps.removeid)
) -> dict:
    data.pop('_id', None)
    return await coll.find_one_and_replace({'_id': _id}, data)


@router.patch('/{coll}/{_id}')
async def patch(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    _id: ObjectId = Depends(deps.objid),
    data: dict = Depends(deps.removeid)
) -> dict:
    data.pop('_id', None)
    return await coll.find_one_and_update({'_id': _id}, data)


@router.post('/{coll}')
async def post(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    data: dict = Depends(deps.removeid)
) -> dict:
    data.pop('_id', None)
    inst = await coll.insert_one(data)
    return await coll.find_one({'_id': inst.inserted_id})


@router.delete('/{coll}/{_id}')
async def delete(
    coll: AsyncIOMotorCollection = Depends(deps.collection),
    _id: ObjectId = Depends(deps.objid)
) -> dict:
    return await coll.find_one_and_delete({'_id': _id})
