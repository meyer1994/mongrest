from fastapi import FastAPI

from mongrest.api.crud import router as router_crud
from mongrest.api.query import router as router_query

app = FastAPI()
app.include_router(router_query)
app.include_router(router_crud)
