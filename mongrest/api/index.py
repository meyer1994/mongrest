from fastapi import APIRouter, Depends

from mongrest.deps.index import FetchIndex, DeleteIndex, CreateIndex


router = APIRouter()


@router.get('/')
async def get(ctx: FetchIndex = Depends(FetchIndex)) -> dict:
    return await ctx.coll.index_information()


@router.post('/', status_code=201)
async def post(ctx: CreateIndex = Depends(CreateIndex)) -> dict:
    return await ctx.coll.create_index(ctx.data)


@router.delete('/{index}')
async def delete(ctx: DeleteIndex = Depends(DeleteIndex)) -> dict:
    return ctx.coll.drop_index(ctx.index, background=True)
