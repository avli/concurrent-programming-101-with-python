import time
from collections import deque
from multiprocessing.pool import ThreadPool

from colorama import Fore

from timer import timer

_thread_pool = ThreadPool(processes=5)


def async_task(target, args, color):
    result = _thread_pool.apply_async(target, args=args)
    while not result.ready():
        print(color + f"{args[0]}: Not yet...")
        yield
    print(color + f"{args[0]}: Done!")
    return result.get()


@timer
def main():
    task_queue = deque([
        async_task(time.sleep, (i,), color) for
        i, color in enumerate([Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA], start=1)
    ])

    while task_queue:
        task = task_queue.popleft()
        try:
            next(task)
            task_queue.append(task)
        except StopIteration:
            pass
        time.sleep(0.5)

    print(Fore.RESET)


if __name__ == '__main__':
    main()
