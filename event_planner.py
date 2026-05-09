from collections import deque
import time


class Sleep:
    def __init__(self,seconds: float):
        self.wake_at = time.monotonic() + seconds


def run(tasks: list):
    ready = deque(tasks)
    sleeping = []
    while ready or sleeping:
        now= time.monotonic()
        still_sleeping = []
        for wake_at, task in sleeping:
            if now >= wake_at:
                ready.append(task)
            else:
                still_sleeping.append((wake_at, task))

        sleeping=still_sleeping


        if not ready:
            time.sleep(0.01)
            continue

        task= ready.popleft()
        try:
            request = next(task)
        except StopIteration:
            continue

        if isinstance(request, Sleep):
            sleeping.append((request.wake_at, task))
        else:
            ready.append(task)



def task_a():
    for i in range(3):
        print(f'A-{i}')
        yield Sleep(0.5)

    print(f'A done')


def task_b():
    for i in range(3):
        print(f'B-{i}')
        yield Sleep(0.3)

    print('B done')

if __name__ == '__main__':
    tasks=[task_a(),task_b()]
    run(tasks)
