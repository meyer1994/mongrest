from fastapi import APIRouter, Depends, HTTPException, status

from pymongo.collection import ReturnDocument

from mongrest.deps.crud import (
    InsertOne,
    FetchOne,
    UpdateOne,
    DeleteOne,
    ReplaceOne
)

AFTER = ReturnDocument.AFTER

router = APIRouter()


@router.post('/', status_code=201)
async def post(dep: InsertOne = Depends(InsertOne)) -> dict:
    dep.data.pop('_id', None)
    inst = await dep.coll.insert_one(dep.data)
    return await dep.coll.find_one({'_id': inst.inserted_id})


@router.get('/{_id}')
async def get(dep: FetchOne = Depends(FetchOne)) -> dict:
    data = await dep.coll.find_one({'_id': dep._id})
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {'data': data}


@router.put('/{_id}')
async def put(dep: ReplaceOne = Depends(ReplaceOne)) -> dict:
    dep.data.pop('_id', None)
    filtr = {'_id': dep._id}
    data = await dep.coll\
        .find_one_and_replace(filtr, dep.data, return_document=AFTER)
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {'data': data}


@router.patch('/{_id}')
async def patch(dep: UpdateOne = Depends(UpdateOne)) -> dict:
    dep.data.pop('_id', None)
    filtr = {'_id': dep._id}
    return await dep.coll\
        .find_one_and_update(filtr, dep.data, return_document=AFTER)


@router.delete('/{_id}')
async def delete(dep: DeleteOne = Depends(DeleteOne)) -> dict:
    data = await dep.coll.find_one_and_delete({'_id': dep._id})
    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return data
