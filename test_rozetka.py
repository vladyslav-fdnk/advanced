import asyncio
import re
import json

import httpx

BASE_URL = "https://rozetka.pl"


async def fetch_category(client, page=1):
    url = f"{BASE_URL}/electronics/c80004/"

    params = {'page': page}


    r = await client.get(url,params=params)
    r.raise_for_status()
    return r.text

def extract_ids(html: str):
    match = re.search(r'window.__INITIAL_STATE__\s*=\s*({.*?});', html)
    if not match:
        return []

    try:
        data = json.loads(match.group(1))
    except (json.JSONDecodeError, TypeError):
        return []

    ids = []

    def walk(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "id" and isinstance(v, (int, str)):
                    ids.append(str(v))
                else:
                    walk(v)
        elif isinstance(obj, list):
            for i in obj:
                walk(i)

    walk(data)

    return list(set(ids))

async def fetch_details(client, ids: list[str]):
    url = "https://common-api.rozetka.pl/v1/api/product/details"

    params = {
        "country": "PL",
        "lang": "ua",
        "ids": ",".join(ids)
    }

    r = await client.get(url, params=params)
    r.raise_for_status()
    return r.json()


async def main():
    async with httpx.AsyncClient(timeout=20,follow_redirects=True) as client:
        html = await fetch_category(client, page=1)

        ids = extract_ids(html)

        print(f"Found IDs: {len(ids)}")

        if not ids:
            print("No products found (site layout may have changed)")
            return

        details = await fetch_details(client, ids[:20])  # лимитируем

        for pid, item in details.get("data", {}).items():
            print(item.get("title"))
            print(item.get("href"))
            print("----")


asyncio.run(main())
