from fastapi import APIRouter, Depends

from mongrest.deps.index import FetchIndex, DeleteIndex, CreateIndex


router = APIRouter()


@router.get('/')
async def get(dep: FetchIndex = Depends(FetchIndex)) -> dict:
    return await dep.coll.index_information()


@router.post('/', status_code=201)
async def post(dep: CreateIndex = Depends(CreateIndex)) -> dict:
    return await dep.coll.create_index(dep.data)


@router.delete('/{index}')
async def delete(dep: DeleteIndex = Depends(DeleteIndex)) -> dict:
    return await dep.coll.drop_index(dep.index, background=True)
