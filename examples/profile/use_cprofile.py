
#%%
import dis

def note() :
    """
        python -m cProfile -s time myscript.py 

        显示工具KCacheGrind，显示Valgrind的输出

        pyprof2calltree将cProfile的输出转化成Valgrind的格式， -o选项
        
        使用pypy，代替CPython

        python -m memory_profiler script.py 

        `memory_profiler <https://pypi.org/project/memory-profiler/>`_

        using memoryview

        time.perf_counter()

        timeit

        profile

    """
    pass 

def x():

    """
    >>> dis.dis(x)
    dis模块对python代码反编译
    """

    return 42



if __name__ == "__main__" :
    dis.dis(x)

    s = b"abcdefgh"
    view = memoryview(s)

    s = set()
    print( [ f for f in dir(s) if not f.startswith("__")])


#%%
