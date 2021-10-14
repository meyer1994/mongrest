from fastapi import APIRouter

from mongrest.deps import Filter, Page


router = APIRouter()


@router.get('/{coll}/_find')
async def find(f=Filter, p=Page) -> list:
    cursor = f.coll.find(f.filter)
    cursor.skip(p.skip)
    return await cursor.to_list(p.size)


@router.delete('/{coll}/_find')
async def delete(f=Filter) -> list:
    result = await f.coll.delete_many(f.filter)
    return result.raw_result


@router.get('/{coll}/_findone')
async def findone(f=Filter) -> dict:
    return await f.coll.find_one(f.filter)


@router.delete('/{coll}/_findone')
async def deleteone(f=Filter) -> dict:
    return await f.coll.find_one_and_delete(f.filter)


@router.post('/{coll}/_aggregate')
async def aggregate(data: list[dict], f=Filter, p=Page) -> list:
    aggreg = [{'$match': f.filter}, *data]
    cursor = f.coll.aggregate(aggreg)
    cursor.skip(p.skip)
    return await cursor.to_list(p.size)


@router.get('/{coll}/_count')
async def count(f=Filter) -> list:
    return await f.coll.count_documents(f.filter)
