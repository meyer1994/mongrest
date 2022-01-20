from fastapi import FastAPI

from mongrest import api

app = FastAPI(debug=True)
app.include_router(api.router)
