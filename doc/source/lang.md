# 语法

```eval_rst
.. automodule:: examples.lang.slots
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: examples.lang.api
   :members:
   :undoc-members:
   :show-inheritance:
```

### inspect

inspect - Get useful information from live Python objects.

### functools

### ABCMeta

six模块是Python为了兼容Python 2.x 和Python 3.x提供的一个模块，该模块中有一个针对类的装饰器 @six.add_metaclass(MetaClass) 可以为两个版本的Python类方便地添加metaclass。这样我们就可以同时利用Python中的abc模块和six模块在类的定义前添加 @six.add_metaclass(abc.ABCMeta) 来优雅地声明一个抽象基础类了！

``` python
    import six
    import abc

    @six.add_metaclass(abc.ABCMeta)
    class PluginBase(object) :
        pass
```

#### super(), mro()

mro
    method resolution order


### util

#### print
```python
num = 1
print(f"coroutine_{num} start")
```