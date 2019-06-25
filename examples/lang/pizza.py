
class Pizza(object) :

    def __init__(self, c, v) :
        self.cheese = c
        self.vegtables = v

    @staticmethod 
    def mix_ingredients(x, y) :
        return x + y

    def cook(self) :
        return self.mix_ingredients(self.cheese, self.vegtables)

    radius = 42
    @classmethod 
    def get_radius(cls):
        return cls.radius

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegtables())

    
#%%
import abc 

class Egg(object):
    pass

class BasePizza(object) :
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
        """return thid gredient list"""

class Calzone(BasePizza) :

    def __init__(self):
        self.ingredients = ["egg"]

    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]

#%%
import abc
import six

@six.add_metaclass(abc.ABCMeta)
class PluginBase(object):

    @abc.abstractmethod
    def func_a(self, data):
        """
        abstract method
        """

    @abc.abstractmethod 
    def func_b(self, output, data):
        """
        another
        """
        pass

class RegisteredImpl(object):

    def func_a(self, data):
        print("override in RegisteredImpl")

class SubclassImpl(PluginBase) :
    def func_a(self, data):
        print("override func_a")

    def func_b(self, output, data):
        print("override func_b")


PluginBase.register(RegisteredImpl)

if __name__ == "__main__":
    for sc in PluginBase.__subclasses__():
        print("subclass : {}".format(sc.__name__))
    
    print( issubclass(SubclassImpl, PluginBase))
    print( isinstance(SubclassImpl(), PluginBase))



#%%
