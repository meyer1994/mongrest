import pydantic
from bson import ObjectId
from pydantic import BaseSettings, AnyUrl

# Adapted from:
#   https://github.com/tiangolo/fastapi/issues/1515#issuecomment-782835977
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


class Settings(BaseSettings):
    mongo_db: str = 'mongrest'
    mongo_host: AnyUrl = 'mongodb://localhost:27017'


settings = Settings()
