# %%
# def exe_bg():
"""
    concurrent.futures + rxpy
"""

import concurrent.futures
import math
import rx
import multiprocessing

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True



# %%


if __name__ == "__main__":
    multiprocessing.freeze_support()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
    # with concurrent.futures.ThreadPoolExecutor() as executor:
        fut = executor.submit( is_prime , PRIMES[0])

        def on_next(x):
            print("on_next = {}".format(x))

        def on_error(err):
            print("on_error = {}".format(err))

        def on_completed():
            print("on_completed = {}".format("complete"))

        rx.from_future(fut).subscribe(on_next, on_error, on_completed)

        concurrent.futures.wait([fut])  #.result()    