from fastapi import APIRouter

from .crud import router as router_crud
from .query import router as router_query
from .admin.index import router as router_index
# from .admin.schema import router as router_schema


router = APIRouter()

# router.include_router(router_schema)
router.include_router(router_index)
router.include_router(router_query)
router.include_router(router_crud)
