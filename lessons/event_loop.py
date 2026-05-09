from collections import deque

ready_queue = deque()
wait_queue = deque()

def event_loop():
    while ready_queue or wait_queue:
        if not ready_queue:
            waith_for_next_event(wait_queue)
        task= ready_queue.popleft()
        try:
            reason = task.run_until_paused()
        except StopIteration:
            continue
        if reason == 'sleep':
            wait_queue.append(task)
        elif reason == 'io':
            wait_queue.append(task)
        else:
            ready_queue.append(task)