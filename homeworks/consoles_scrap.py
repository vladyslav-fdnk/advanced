from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import requests
from selectolax.parser import HTMLParser


def get_response(url: str) -> str :
    with requests.Session() as session:
        response = session.get(url, timeout=5)
        assert response.status_code == 200, 'Wrong status code'

    return response.text


def parse_detail_item(html: str) -> str:
    tree = HTMLParser(html)
    data = tree.css('h1')[0].text(strip=True)
    return data


def get_detail(queue: Queue) -> None:
    while not queue.empty():
        link = queue.get()
        html_response = get_response(link)
        result = parse_detail_item(html_response)
        print(f'Parsed {link} with result: {result}')


if __name__ == '__main__':
    main_url = 'https://rozetka.pl/ua/konsole-do-gier-i-konsole-dla-dzieci-80020/c80020//'
    response_html = get_response(main_url)
    tree = HTMLParser(response_html)
    links = [link.attributes['href'] for link in tree.css('.tile-image-host')]
    print(f'Found {len(links)} links to parse')

    queue = Queue()
    for item in links:
        queue.put(item)

    with ThreadPoolExecutor(max_workers=40) as executor:
        for _ in range(40):
            executor.submit(get_detail, queue)