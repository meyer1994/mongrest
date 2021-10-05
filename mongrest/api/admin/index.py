from fastapi import APIRouter

router = APIRouter()


@router.get('/{coll}/_index/{name}')
async def get(coll: str, name: str) -> dict:
    pass


@router.post('/{coll}/_index')
async def post(coll: str, data: dict) -> dict:
    pass


@router.delete('/{coll}/_index/{name}')
async def delete(coll: str) -> dict:
    pass
