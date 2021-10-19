from fastapi import APIRouter, Depends

import mongrest.deps.query as deps


router = APIRouter()


@router.get('/_find')
async def find(req=Depends(deps.PagedQuery)) -> list:
    cursor = req.coll.find(req.query)
    cursor.skip(req.page._skip)
    return await cursor.to_list(req.page._size)


@router.delete('/_find')
async def delete(req=Depends(deps.Query)) -> list:
    result = await req.coll.delete_many(req.query)
    return result.raw_result


@router.get('/_findone')
async def findone(req=Depends(deps.Query)) -> dict:
    return await req.coll.find_one(req.query)


@router.delete('/_findone')
async def deleteone(req=Depends(deps.Query)) -> dict:
    return await req.coll.find_one_and_delete(req.query)


@router.post('/_aggregate')
async def aggregate(req=Depends(deps.AggregateQuery)) -> list:
    aggreg = [{'$match': req.query}, *req.data]
    cursor = req.coll.aggregate(aggreg)
    cursor.skip(req.page._skip)
    return await cursor.to_list(req.page._size)


@router.get('/_count')
async def count(req=Depends(deps.Query)) -> list:
    return await req.coll.count_documents(req.query)
