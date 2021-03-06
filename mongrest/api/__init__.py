from fastapi import APIRouter

from . import rest
from . import index
from . import schema
from . import realtime

router = APIRouter()

# API
router.include_router(rest.router, prefix='/rest/{coll}')
router.include_router(realtime.router, prefix='/realtime/{coll}')

# Admin
router.include_router(index.router, prefix='/index/{coll}')
router.include_router(schema.router, prefix='/schema/{coll}')

# Files
# coming soon!
