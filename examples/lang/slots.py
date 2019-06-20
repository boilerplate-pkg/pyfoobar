
#%%
class Point(object):

    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

def use_namedtuple() :
    """
    collections.namedtuple("Foobar", ["x", "y"])
    """
    import collections
    FooBar = collections.namedtuple("FooBar", ["x", "y"])
    fb = FooBar(x=43, y=42)

    print(fb)
    print(fb._asdict())
    print(fb._make([2,3]))
    print(fb._replace(x=1))


#%%
