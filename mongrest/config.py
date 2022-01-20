import pydantic
from bson import ObjectId, Timestamp
from pydantic import BaseSettings, AnyUrl

# Adapted from:
#   https://github.com/tiangolo/fastapi/issues/1515#issuecomment-782835977
pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str
pydantic.json.ENCODERS_BY_TYPE[Timestamp] = lambda t: t.as_datetime().isoformat()  # noqa


class Settings(BaseSettings):
    mongo_db: str = 'mongrest'
    mongo_host: AnyUrl = 'mongodb://root:password@localhost:27017'  # noqa


settings = Settings()
