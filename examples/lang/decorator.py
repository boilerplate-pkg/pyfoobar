#%%
def identity(f):
    return f

@identity
def foo() :

    return "bar"

#%%
import functools

def check_is_admin(f):

    """
    functools.update_wrapper
    functools.wraps: copy __doc__ to wrapper
    """
    @functools.wraps(f) # import functools, 
    def wrapper(*args, **kwargs):
        if kwargs.get("username") != "admin":
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)

#%%
import functools
# help(functools.wraps)

#%%
# print(functools.__doc__)

#%%
import inspect

def check_is_admin2(f) :
    """
    inspect: check if has arg or not
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        if func_args.get("username") != "admin" :
            raise Exception("this user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

@check_is_admin2
def get_food(username, type="chocolate"):
    return type+" mnkk"



#%%
def use_inspect() :
    d = { "d" : "c"}
    inspect.getmembers(d)
