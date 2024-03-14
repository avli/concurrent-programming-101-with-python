import time
from collections import deque
from multiprocessing.pool import ThreadPool

from colorama import Fore

from timer import timer

_thread_pool = ThreadPool(processes=5)


def async_task(target, args):
    result = _thread_pool.apply_async(target, args=args)
    while not result.ready():
        yield
    return result.get()


@timer
def main():
    task_queue = deque([
        async_task(time.sleep, (i,)) for i in range(1, 6)
    ])

    while task_queue:
        task = task_queue.popleft()
        try:
            next(task)
            task_queue.append(task)
        except StopIteration:
            pass
        time.sleep(0.5)


if __name__ == '__main__':
    main()
