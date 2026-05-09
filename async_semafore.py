import asyncio
import random


semafor = asyncio.Semaphore(10)
queue=asyncio.Queue()


async def fetch():
    await asyncio.sleep(random.random())


async def fetch_polite():
    async with semafor:
        return await fetch()


async def producer():
    for i in range(10):
        await queue.put(i)
    await queue.put(None)


async def consumer():
    while True:
        item = await queue.get()
        if item is None:
            break
        print('consuming', item)


async def main():
    results= await asyncio.gather(
        producer(),
        consumer()
    )
    return results

asyncio.run(main())