from fastapi import APIRouter

from . import query
from . import index
from . import schema
from . import realtime

router = APIRouter()

# API
router.include_router(query.router, prefix='/rest/{coll}')
router.include_router(realtime.router, prefix='/realtime/{coll}')

# Admin
router.include_router(index.router, prefix='/admin/index/{coll}')
router.include_router(schema.router, prefix='/admin/schema/{coll}')

# Files
# coming soon!
