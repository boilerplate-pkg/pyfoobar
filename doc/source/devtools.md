
# 开发环境与工具

## 虚拟环境

### virtual env

```python
virtualenv venv --system-site-package
```

## lint

## test

### unit test

test_打头的文件和函数

### nosetests

### tox

## ci

TODO 工作流

gerrit：代码审查
Jenkins：CI
Travis：代码的签入后运行测试
Zuul: 工作流
Sonar：质量检查和展示

## profile

```eval_rst
.. automodule:: examples.profile.use_cprofile
   :members:
   :undoc-members:
   :show-inheritance:
```

## API变化

sphinx标记

```
    .. deprecated:: 1.1
```

warnings 模块，warnings.warn()

```python
    warnings.warn("turn_left is deprecated sin Version 1.1, use trun instead")
```

debtcollector模块标注
``` python
    from debtcollector import moves
    @move.moved_method("turn",version="1.1")
```
