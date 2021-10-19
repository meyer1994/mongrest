from fastapi import APIRouter, Depends

from mongrest import deps


router = APIRouter()


@router.post('/{coll}')
async def post(req=Depends(deps.InsertOne)) -> dict:
    inst = await req.coll.insert_one(req.data)
    return await req.coll.find_one({'_id': inst.inserted_id})


@router.get('/{coll}/{_id}')
async def get(req=Depends(deps.FetchOne)) -> dict:
    return await req.coll.find_one({'_id': req._id})


@router.put('/{coll}/{_id}')
async def put(req=Depends(deps.UpdateOne)) -> dict:
    req.data.pop('_id', None)
    return await req.coll.find_one_and_replace({'_id': req._id}, req.data)


@router.patch('/{coll}/{_id}')
async def patch(req=Depends(deps.UpdateOne)) -> dict:
    req.data.pop('_id', None)
    return await req.coll.find_one_and_update({'_id': req._id}, req.data)


@router.delete('/{coll}/{_id}')
async def delete(req=Depends(deps.DeleteOne)) -> dict:
    return await req.coll.find_one_and_delete({'_id': req._id})
