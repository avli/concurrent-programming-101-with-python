from collections import deque
from time import time, sleep

from colorama import Fore

from timer import timer


def async_delay(seconds, color):
    start = time()
    end = start + seconds
    while time() < end:
        print(color + 'Too early...')
        yield
    print(color + f'{seconds} seconds have passed!')


@timer
def main():
    tasks = [async_delay(1, color) for color in
             [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]]
    task_queue = deque(tasks)
    while task_queue:
        task = task_queue.popleft()
        try:
            next(task)
        except StopIteration:
            continue
        task_queue.append(task)
        sleep(0.1)


if __name__ == '__main__':
    main()
