from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("Elapsed time: ", end - start)
        return result
    return wrapper
