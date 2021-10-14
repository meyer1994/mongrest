from fastapi import APIRouter

from mongrest.deps import Doc, Coll


router = APIRouter()


@router.get('/{coll}/{_id}')
async def get(d=Doc) -> dict:
    return await d.coll.find_one({'_id': d._id})


@router.put('/{coll}/{_id}')
async def put(data: dict, d=Doc) -> dict:
    data.pop('_id', None)
    return await d.coll.find_one_and_replace({'_id': d._id}, data)


@router.patch('/{coll}/{_id}')
async def patch(data: dict, d=Doc) -> dict:
    data.pop('_id', None)
    return await d.coll.find_one_and_update({'_id': d._id}, data)


@router.post('/{coll}')
async def post(data: dict, coll=Coll) -> dict:
    inst = await coll.insert_one(data)
    return await coll.find_one({'_id': inst.inserted_id})


@router.delete('/{coll}/{_id}')
async def delete(d=Doc) -> dict:
    return await d.coll.find_one_and_delete({'_id': d._id})
