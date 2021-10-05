import pydantic
from bson import ObjectId
from pydantic import BaseSettings, AnyUrl

# Adapted from:
#   https://github.com/tiangolo/fastapi/issues/1515#issuecomment-782835977
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


class Settings(BaseSettings):
    mongo_db: str = 'dev'
    mongo_host: AnyUrl = 'mongodb://localhost:27017'
    page_size: int = 10


settings = Settings()
