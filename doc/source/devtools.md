
# 开发环境与工具

## 虚拟环境

### virtual env

```python
virtualenv create venv
```

## lint

## test

### unit test

## ci

## profile
.. automodule:: examples.profile.use_cprofile
   :members:
   :undoc-members:
   :show-inheritance:

## API变化

sphinx标记 .. deprecated:: 1.1

    .. deprecated:: 1.1

warnings 模块，warnings.warn()

    warnings.warn("turn_left is deprecated sin Version 1.1, use trun instead")

debtcollector模块标注

    from debtcollector import moves
    @move.moved_method("turn",version="1.1")

.. automodule:: examples.lang.api
   :members:
   :undoc-members:
   :show-inheritance: