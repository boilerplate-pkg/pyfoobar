#%%
import bisect

#help(bisect)

#%%
def use_bisect() :
    """
    bisect
        二分查找

    blist，bintree
        二叉树和红黑树
    """
    farm = sorted(["x", "g", "h", "c"])
    print(farm)
    
    index = bisect.bisect_right(farm, "h")
    print(farm[:index])

    index = bisect.bisect_left(farm, "h")
    print(farm[:index])

    bisect.insort_left(farm, "h")
    print(farm)

    bisect.insort(farm, "h")
    print(farm)


# use_bisect()
#%%
# import blist 
# import bintree