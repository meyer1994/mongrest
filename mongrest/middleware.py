import time

from fastapi import Request, Response


async def servertime(req: Request, cnext: callable) -> Response:
    start = time.time()
    res = await cnext(req)
    end = time.time()
    total = (end - start) * 1000  # ms
    res.headers['X-Server-Time'] = f'{total}ms'
    return res
