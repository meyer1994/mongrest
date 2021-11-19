from fastapi import APIRouter, Depends

from mongrest.deps.schema import FetchSchema, CreateSchema, DeleteSchema


router = APIRouter()


@router.get('/_schema')
async def get(dep: FetchSchema = Depends(FetchSchema)) -> dict:
    filtr = {'name': dep.coll}
    cursor = await dep.db.list_collections(filter=filtr)

    for info in cursor:
        return info.get('options', {})\
            .get('validator', {})\
            .get('$jsonSchema', {})

    return


@router.post('/_schema')
async def post(dep: CreateSchema = Depends(CreateSchema)) -> dict:
    command = {
        'collMod': dep.coll,
        'validator': {'$jsonSchema': dep.schema}
    }
    return await dep.db.command(command)


@router.delete('/_schema')
async def delete(dep: DeleteSchema = Depends(DeleteSchema)) -> dict:
    command = {
        'collMod': dep.coll,
        'validator': {'$jsonSchema': {}}
    }
    return await dep.db.command(command)
