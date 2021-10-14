from fastapi import FastAPI

from mongrest.api import router
from mongrest.middleware import servertime


app = FastAPI()

app.include_router(router)
app.middleware('http')(servertime)
