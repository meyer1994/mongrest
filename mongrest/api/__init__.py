from fastapi import APIRouter

from .crud import router as router_crud
from .index import router as router_index
from .query import router as router_query
from .schema import router as router_schema


router = APIRouter(prefix='/{coll}')

router.include_router(router_schema)
router.include_router(router_index)
router.include_router(router_query)
router.include_router(router_crud)
