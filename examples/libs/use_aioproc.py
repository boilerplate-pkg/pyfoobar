#%%
import time
import asyncio
import aioprocessing
import multiprocessing
import rx
import math

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def on_next(x):
    print("on_next = {}".format(x))

def on_error(err):
    print("on_error = {}".format(err))

def on_completed():
    print("on_completed = {}".format("complete"))

if __name__ == "__main__":
    multiprocessing.freeze_support()

    p = aioprocessing.AioProcess(target=is_prime, args=(115797848077099,))
    p.start()
    fut = asyncio.ensure_future(p.coro_join())

    rx.from_future(fut).subscribe(on_next, on_error, on_completed)
