import time
from asyncio import tasks

import httpx
import asyncio
from selectolax.parser import HTMLParser


async def worker(qu: asyncio.Queue, session: httpx.AsyncClient):
    while not qu.empty():
        link = qu.get()
        print(f'working on {link}, queue size: {qu.qsize()}')
        try:
            response = await session.get(main.main_url)
            tree = HTMLParser(response.text)
            print()
        except (httpx.ConnectError, httpx.ConnectTimeout) as e:
            print('request error',e)
            await qu.put(link)
        except Exception as e:
            print('general exception',e)


async def main():
    main_url= "https://rozetka.pl/ua/laptopy-80004/c80004/"
    session = httpx.AsyncClient()
    response = await session.get(main_url)
    tree= HTMLParser(response.text)
    # print(tree.css('.item .tile-imaggge-host'))
    links = [link.attributes ['href'] for link in tree.css('.item a')]
    print(f' number of links: {len(links)}')
    links_queue = asyncio.Queue()
    for link in links:
        links_queue.put_nowait(link)

    for _ in range(len(links)):
        task= worker(links_queue, session)
        tasks.append(task)

    await asyncio.gather(*tasks)




if __name__ == "__main__":
    start=time.time()
    asyncio.run(main())
    end=time.time()
    print(f'{end-start} seconds')
