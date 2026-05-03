import queue
import threading
import time

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def worker(name: str,seconds: int) -> None:
    print(f'Working on {name}, starting')
    time.sleep(seconds)
    print(f'Working on {name}, finished in {seconds} seconds')


counter=0
lock = threading.Lock()


def incremen_milion_times():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter+=1

queue=queue.Queue()
for i in range(20):
    queue.put(i)

def worker_queue():
    while not queue.empty():
        item=queue.get()
        print(f'Working on {item}')


def fake_http_request(i: int) -> int:
    time.sleep(1)
    return i

def run_serial():
    start = time.perf_counter()
    for i in range(20):
        fake_http_request(i)
    print(f'serial executed in {time.perf_counter() - start:.2f} seconds')

def run_threaded():
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=20) as executor:
        list(executor.map(fake_http_request, range(20)))
    print(f'threaded executed in {time.perf_counter() - start:.2f} seconds')


def heavy_computation(number: int):
    total = 0
    for i in range(number):
        total += i*i

    return total


def run_serial_heavy():
    start = time.perf_counter()
    for i in range(4):
        heavy_computation(50_000_000)
    print(f'serial executed in {time.perf_counter() - start:.2f} seconds')

def run_threaded_heavy():
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_computation, [50000000]* 4))
    print(f'threaded executed in {time.perf_counter() - start:.2f} seconds')


if __name__ == '__main__':
    # worker( 'A', 1)
    # worker( 'B', 2)
    # worker( 'C',3)

    # t1=threading.Thread(target=worker, args=('A',1))
    # t2=threading.Thread(target=worker, args=('B',2))
    # t3=threading.Thread(target=worker, args=('C',3))
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # print('All done!')

    # threads=[threading.Thread(target=incremen_milion_times) for _ in range(5)]
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    # print(f'Counter value: {counter}')

    # threads=[threading.Thread(target=worker_queue) for _ in range(4)]
    # for t in threads:
    #     t.start()
    # for t in threads:
    #     t.join()
    #
    # print('all done')
    #

    #
    # run_serial()
    # run_threaded()

    run_serial_heavy()
    run_threaded_heavy()

    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(heavy_computation, [50_000_000]*4))
    print(f'Process execution took {time.perf_counter()}')