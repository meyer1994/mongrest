from fastapi import APIRouter, Depends

import mongrest.deps.index as deps


router = APIRouter()


@router.get('/_index')
async def get(coll=Depends(deps.Collection)) -> dict:
    return await coll.index_information()


@router.post('/_index')
async def post(req=Depends(deps.CreateIndex)) -> dict:
    return await req.coll.create_index(req.data)


@router.delete('/_index/{index}')
async def delete(req=Depends(deps.DeleteIndex)) -> dict:
    return await req.coll.drop_index(req.index, background=True)
