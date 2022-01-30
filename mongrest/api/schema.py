from fastapi import APIRouter, Depends

from mongrest.deps.schema import FetchSchema, CreateSchema, DeleteSchema


router = APIRouter()


@router.get('/')
async def get(ctx: FetchSchema = Depends(FetchSchema)) -> dict:
    filtr = {'name': ctx.coll}
    cursor = await ctx.db.list_collections(filter=filtr)

    for info in cursor:
        return info.get('options', {})\
            .get('validator', {})\
            .get('$jsonSchema', {})

    return {}


@router.post('/', status_code=201)
async def post(ctx: CreateSchema = Depends(CreateSchema)) -> dict:
    command = {
        'collMod': ctx.coll,
        'validator': {'$jsonSchema': ctx.schema}
    }
    return await ctx.db.command(command)


@router.delete('/')
async def delete(ctx: DeleteSchema = Depends(DeleteSchema)) -> dict:
    command = {
        'collMod': ctx.coll,
        'validator': {'$jsonSchema': {}}
    }
    return await ctx.db.command(command)
