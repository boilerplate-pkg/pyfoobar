#%%
import functools 
import math

@functools.lru_cache(maxsize = 2)
def memoized_sin(x):
    """
    functools.lru_cache(maxsize)
    """
    return math.sin(x)

if __name__ == "__main__" :
    memoized_sin(2)
    memoized_sin.cache_info()
    memoized_sin(2)
    memoized_sin.cache_clear()
    memoized_sin.cache_info()