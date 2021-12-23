from fastapi import FastAPI

from mongrest import api


app = FastAPI()
app.include_router(api.router)
