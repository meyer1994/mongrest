import httpx
from fastapi import APIRouter, Request

from mongrest.config import settings


router = APIRouter()


@router.post('/token')
async def token(req: Request) -> dict:
    params = await req.form()
    res = httpx.post(settings.jwt_url, params=params)
    res.raise_for_status()
    return res.json()
