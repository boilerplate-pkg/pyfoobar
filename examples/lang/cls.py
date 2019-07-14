#%%

def id(cls) :
    cls.id = cls.__module__ + "." + cls.__name__
    return cls

@id
class Cls(object):

    pass

if __name__ == "__main__" :
    print(Cls.id)

#%%
