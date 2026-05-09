import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing.dummy import Queue
# from queue import Queue
from selectolax.parser import HTMLParser
from time import perf_counter


def get_response(url: str) -> str:
    with requests.Session() as session:
        response = session.get(url, timeout=5)
        assert response.status_code == 200, 'Wrong status code'
        return response.text


def get_session_response(url: str, session: requests.Session) -> str:
    response = session.get(url, timeout=5)
    assert response.status_code == 200, 'Wrong status code'
    return response.text


def parse_detail_item(html: str) -> str:
    tree = HTMLParser(html)
    h1 = tree.css_first('h1')
    return h1.text(strip=True) if h1 else 'No title'


def get_detail(queue: Queue):
    with requests.Session() as session:
        while True:
            try:
                link = queue.get_nowait()
            except:
                break

            html_response = get_session_response(link, session)
            result = parse_detail_item(html_response)

            print(f'{result} | {link}')


if __name__ == '__main__':
    workers= 8
    start = perf_counter()

    main_url = 'https://rozetka.pl/ua/laptopy-80004/c80004/'
    response_html = get_response(main_url)

    tree = HTMLParser(response_html)

    links = [link.attributes.get('href') for link in tree.css('.title-image-host') if link.attributes.get('href')]
    print(f'found {len(links)} links')

    # queue = Queue()
    # for item in links:
    #     queue.put(item)

    urls_links_count = len(links)
    chunks = round(urls_links_count / workers)
    url_links = [links[i:i + workers] for i in range(0, len(links), chunks)]
    print(url_links)




        with ProcessPoolExecutor(max_workers=4) as executor:
            for links_list in url_links:
                executor.submit(get_detail_processes, links_list)

    print(f'finished in {perf_counter() - start:.2f} seconds')