from fastapi import APIRouter, Depends

from mongrest.deps.rest import Query, PagedQuery, InsertOne


router = APIRouter()


@router.get('/')
async def get(ctx: PagedQuery = Depends(PagedQuery)) -> list:
    cursor = ctx.coll.find(ctx.query)
    cursor.skip(ctx.page.skip)
    return await cursor.to_list(ctx.page.limit)


@router.post('/', status_code=201)
async def post(ctx: InsertOne = Depends(InsertOne)) -> dict:
    inst = await ctx.coll.insert_one(ctx.data)
    return await ctx.coll.find_one({'_id': inst.inserted_id})


@router.delete('/')
async def delete(ctx: Query = Depends(Query)) -> list:
    result = await ctx.coll.delete_many(ctx.query)
    result.raw_result.pop('$clusterTime', None)
    return result.raw_result
