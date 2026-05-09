import time
import httpx
import asyncio
import re
#import pandas as pd

#
from selectolax.parser import HTMLParser

main_url= "https://rozetka.pl/ua/laptopy-80004/c80004/"



async def worker(qu: asyncio.Queue, session: httpx.AsyncClient):
    while not qu.empty():
        link = await qu.get()
        print(f'working on {link}, queue size: {qu.qsize() if qu.qsize()>=0 else len(link)}')
        print(f'extract id {extract_id(link)}')
        try:
            response = await session.get(main_url + link,timeout=5)
            tree = HTMLParser(response.text)
            # print('Title', tree.css('h1')[0].text(strip=True))
            title_node = tree.css_first("tile-title black-link text-base")
            if title_node:
                title = tree.css_first("tile-title black-link text-base").text()
                print(title)
        except (httpx.ConnectError, httpx.ConnectTimeout) as e:
            print('request error',e)
            await qu.put(link)
        except Exception as e:
            pass
            print('general exception',e)

def extract_id(url: str) -> str | None:
    match = re.search(r"(\d+)(?:/)?$", url)
    return match.group(1) if match else None




async def main():
    session = httpx.AsyncClient()
    response = await session.get(main_url)
    tree= HTMLParser(response.text)

    links = []

    for link in tree.css('.item a'):
        href = link.attributes.get('href')

        if not href:
            continue

        if "/comments/" in href:
            continue

        if "/p" not in href:
            continue

        links.append(href)

    links = list(set(links))

    print(f' number of links: {len(links)}')
    links_queue = asyncio.Queue()
    for link in links:
        links_queue.put_nowait(link)

    tasks = []
    for _ in range(len(links)):
        task= worker(links_queue, session)
        tasks.append(task)

    await asyncio.gather(*tasks)




if __name__ == "__main__":
    start=time.time()
    asyncio.run(main())
    end=time.time()
    print(f'{end-start} seconds')
