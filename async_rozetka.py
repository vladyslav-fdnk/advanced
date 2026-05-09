import time
import httpx
import asyncio
import re
import sqlite3
import json
#import pandas as pd

from selectolax.parser import HTMLParser

main_url= "https://rozetka.pl/ua/laptopy-80004/c80004/"


def extract_id(url: str) -> str | None:
    match = re.search(r"(\d+)(?:/)?$", url)
    return match.group(1) if match else None

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY
)
""")



async def worker(qu: asyncio.Queue, session: httpx.AsyncClient):
    while True:
        try:
            link = await qu.get()

            product_id=extract_id(link)

            if not product_id:
                continue


            print(f'working on {link}, queue size: {qu.qsize() if qu.qsize()>=0 else len(link)}')
            print(f'extract id {product_id}')

            api_url = "https://common-api.rozetka.pl/v1/api/product/details"
            params = {
                "country": "PL",
                "lang": "ua",
                "ids": product_id
            }

            api_response = await session.get(
                api_url,
                params=params,
                timeout=10
            )

            api_response.raise_for_status()

            data = api_response.json()

            if not data.get("data"):
                print(f'No data for {product_id}')
                qu.task_done()
                continue

            item = data["data"][0]
            for key, value in item.items():
                if isinstance(value, (dict, list)):
                    value = json.dumps(value, ensure_ascii=False)

                column_type = "TEXT"

                if isinstance(value, int):
                    column_type = "INTEGER"

                elif isinstance(value, float):
                    column_type = "REAL"

                try:
                    cursor.execute(
                        f'ALTER TABLE products ADD COLUMN "{key}" {column_type}'
                    )
                except sqlite3.OperationalError:
                    pass

            json_data = json.dumps(item, ensure_ascii=False)

            cursor.execute("""
            INSERT OR REPLACE INTO products (id, json)
            VALUES (?, ?)
            """, (
                int(product_id),
                json_data
            ))

            conn.commit()

            print(f'SAVED {product_id}')

        except (httpx.ConnectError, httpx.ConnectTimeout) as e:
            print('request error', e)
            await qu.put(link)

        except Exception as e:
            print('general exception', e)
        finally:
            qu.task_done()



def get_product(product_id: int) -> dict:
    url = "https://common-api.rozetka.pl/v1/api/product/details"

    params = {
        "country": "PL",
        "lang": "ua",
        "ids": product_id
    }
    response = httpx.get(
        url,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    return response.json()





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
    for _ in range(10):
        task = asyncio.create_task(
    worker(links_queue, session)
)
        tasks.append(task)
    
    await links_queue.join()

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks)

    await session.aclose()

    conn.close()




if __name__ == "__main__":
    start=time.time()
    asyncio.run(main())
    end=time.time()
    print(f'{end-start} seconds')
    
