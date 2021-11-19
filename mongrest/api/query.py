from fastapi import APIRouter, Depends

from mongrest.deps.query import PagedQuery, Query, AggregateQuery


router = APIRouter()


@router.get('/_find')
async def find(req: PagedQuery = Depends(PagedQuery)) -> list:
    print(req)
    cursor = req.coll.find(req.query)
    cursor.skip(req.page.skip)
    return await cursor.to_list(req.page.size)


@router.delete('/_find')
async def delete(req: Query = Depends(Query)) -> list:
    result = await req.coll.delete_many(req.query)
    return result.raw_result


@router.get('/_findone')
async def findone(req: Query = Depends(Query)) -> dict:
    return await req.coll.find_one(req.query)


@router.delete('/_findone')
async def deleteone(req: Query = Depends(Query)) -> dict:
    return await req.coll.find_one_and_delete(req.query)


@router.get('/_count')
async def count(req: Query = Depends(Query)) -> list:
    return await req.coll.count_documents(req.query)
