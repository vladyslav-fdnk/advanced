import os
import multiprocessing
from time import sleep


def worker(name: str) -> None:
    print(f'working on {name} my id is {os.getpid()}')
    sleep(5)


if __name__ == '__main__':
    print(f'main process: {os.getpid()}')
    # process=multiprocessing.Process(target=worker, args=('Child process',))
    # process.start()
    # process.join()
    print(multiprocessing.cpu_count())
    print(multiprocessing.get_start_method())
    print('main process finished')


