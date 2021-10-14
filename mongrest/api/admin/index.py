from fastapi import APIRouter

from mongrest.deps import Coll


router = APIRouter()


@router.get('/{coll}/_index/{index}')
async def get(index: str, coll=Coll) -> dict:
    pass


@router.post('/{coll}/_index')
async def post(data: dict, coll=Coll) -> dict:
    pass


@router.delete('/{coll}/_index/{index}')
async def delete(index: str, coll=Coll) -> dict:
    pass
