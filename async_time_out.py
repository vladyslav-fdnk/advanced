import asyncio

import requests


async def slow():
    await asyncio.sleep(1)


async def slow_async_input_output():
    try:
        async with asyncio.timeout(2):
            await slow()
    except asyncio.TimeoutError:
        print('This coroutine timed out.')



async def fetch_requests(url):
    return await asyncio.to_thread(requests.get,url)