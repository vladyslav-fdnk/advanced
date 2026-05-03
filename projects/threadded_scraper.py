import requests
from concurrent.futures import ThreadPoolExecutor

from queue import Queue
from selectolax.parser import HTMLParser

from threads import queue


def get_response(url: str) -> str:
    with requests.Session() as session:
        response = session.get(url,timeout=5)
        assert response.status_code == 200, 'Wrong status code'

    return response.text


def parse_detail_item(html: str) -> str:
    tree = HTMLParser(html)
    data=tree.css('h1')[0].text(strip=True)
    # print(data)
    return data

def get_detail(queue: Queue):
    while not queue.empty():
        link=queue.get()
        # print(link)
        html_response=get_response(link)
        # print(html_response)
        result=parse_detail_item(html_response)
        print(f'Parsing detail item from {link}')



if __name__ == '__main__':
    main_url='https://rozetka.com.ua/ua/notebooks/c80004/'
    response = get_response(main_url)
    tree = HTMLParser(response_html)
    links=[link.atributes['href'] for link in tree.css('.title-image-host')]
    print(f'found {len(links)} links')

    queue = Queue()
    for item in links:
        queue.put(item)



    with ThreadPoolExecutor(max_workers=1) as executor:
        for _ in range(1):
            executor.submit(get_detail, queue)
