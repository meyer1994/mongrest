from fastapi import APIRouter

router = APIRouter()


@router.get('/_schema')
async def get(coll: str) -> dict:
    pass


@router.post('/_schema')
async def post(coll: str, data: dict) -> dict:
    pass


@router.delete('/_schema')
async def delete(coll: str) -> dict:
    pass
