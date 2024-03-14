from time import time, sleep

from colorama import Fore

from timer import timer


def sync_delay(seconds, color):
    start = time()
    end = start + seconds
    while time() < end:
        print(color + 'Too early...')
        sleep(0.5)
    print(color + f'{seconds} seconds have passed!')


@timer
def main():
    for color in Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA:
        sync_delay(1, color)
    print(Fore.RESET)


if __name__ == '__main__':
    main()
