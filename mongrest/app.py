from fastapi import FastAPI

from mongrest import api
from mongrest import middleware


app = FastAPI()
app.include_router(api.router)
app.middleware('http')(middleware.servertime)
