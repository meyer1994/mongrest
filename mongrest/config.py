import pydantic
from bson import ObjectId
from pydantic import BaseSettings, AnyUrl

# Adapted from:
#   https://github.com/tiangolo/fastapi/issues/1515#issuecomment-782835977
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str


class Settings(BaseSettings):
    mongo_db: str = 'dev'
    mongo_host: AnyUrl = 'mongodb://localhost:27017'
    jwt_url: str = 'http://localhost:9999/token'  # gotrue's default api url
    jwt_secret: str = 'secret'
    jwt_algorithm: str = 'HS256'


settings = Settings()
