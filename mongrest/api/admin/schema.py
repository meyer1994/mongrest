from fastapi import APIRouter

router = APIRouter()


@router.get('/{coll}/_schema')
async def get(coll: str) -> dict:
    pass


@router.post('/{coll}/_schema')
async def post(coll: str, data: dict) -> dict:
    pass


@router.delete('/{coll}/_schema')
async def delete(coll: str) -> dict:
    pass
