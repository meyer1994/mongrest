import asyncio
from contextlib import asynccontextmanager

from bson import Timestamp
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from starlette.websockets import WebSocket, WebSocketDisconnect

from mongrest.deps.realtime import Query

router = APIRouter()


class Change(BaseModel):
    _id: dict
    ns: dict
    documentKey: dict
    fullDocument: dict
    operationType: str
    clusterTime: Timestamp

    class Config:
        arbitrary_types_allowed = True


async def close(ws: WebSocket):
    while True:
        try:
            await ws.receive_text()
        except WebSocketDisconnect:
            return


async def consume(ws: WebSocket, ctx: Query):
    aggr = [{'$match': ctx.query}]

    watcher = ctx.coll.watch(pipeline=aggr, full_document='updateLookup')

    async with watcher as stream:  # noqa
        async for change in stream:
            change = Change(**change)
            change = change.json()
            await ws.send_text(change)


@router.websocket('/')
async def websocket(ws: WebSocket, ctx: Query = Depends(Query)):
    await ws.accept()

    closer = close(ws)
    closer = asyncio.create_task(closer, name='closer')
    consumer = consume(ws, ctx)
    consumer = asyncio.create_task(consumer, name='consumer')

    tasks = {closer, consumer}

    done, pending = await asyncio\
        .wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for item in pending:
        item.cancel()

    await ws.close()
