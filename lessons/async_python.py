import asyncio
import time


def slow_sync_input_output():
    time.sleep(1) # mocking slow http call


def main_sync():
    start=time.perf_counter()
    for _ in range(10):
        slow_sync_input_output()
    print(f'sync time: { time.perf_counter() - start:.2f}s')


async def slow_async_input_output():
    await asyncio.sleep(1)


async def main_async():
    start=asyncio.get_event_loop().time()

    tasks=[ slow_async_input_output() for _ in range(10) ]
    await asyncio.gather(*tasks)
    print(f'async time: { time.perf_counter() - start:.2f}s')

if __name__ == '__main__':
    asyncio.run(main_async())