from fastapi import APIRouter, Depends

from mongrest.deps.index import (
    FetchIndex,
    DeleteIndex,
    CreateIndex
)


router = APIRouter()


@router.get('/_index')
async def get(dep: FetchIndex = Depends(FetchIndex)) -> dict:
    return await dep.coll.index_information()


@router.post('/_index')
async def post(dep: CreateIndex = Depends(CreateIndex)) -> dict:
    return await dep.coll.create_index(dep.data)


@router.delete('/_index/{index}')
async def delete(dep: DeleteIndex = Depends(DeleteIndex)) -> dict:
    return await dep.coll.drop_index(dep.index, background=True)
