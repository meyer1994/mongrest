from fastapi import APIRouter, Depends

from mongrest.deps.query import Query, PagedQuery, InsertOne


router = APIRouter()


@router.get('/')
async def get(req: PagedQuery = Depends(PagedQuery)) -> list:
    cursor = req.coll.find(req.query)
    cursor.skip(req.page.skip)
    return await cursor.to_list(req.page.size)


@router.post('/', status_code=201)
async def post(ctx: InsertOne = Depends(InsertOne)) -> dict:
    ctx.data.pop('_id', None)
    inst = await ctx.coll.insert_one(ctx.data)
    return await ctx.coll.find_one({'_id': inst.inserted_id})


@router.delete('/')
async def delete(req: Query = Depends(Query)) -> list:
    result = await req.coll.delete_many(req.query)
    return result.raw_result
