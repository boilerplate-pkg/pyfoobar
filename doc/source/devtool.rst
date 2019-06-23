.. _topics-工具支持:

================
开发工具支持
================

参考
================

Full Stack Python https://www.fullstackpython.com/


包管理
================

引入外部包：导入路经设置，导入勾子

pip<https://pip.readthedocs.io/en/stable/user_guide>

库
================


    库的使用::

        标准库
        外部库
        框架

        选用标准：python兼容，开发活跃，维护活跃，与发行版打包，API向后兼容，版权

语言
================

.. automodule:: examples.lang.slots
   :members:
   :undoc-members:
   :show-inheritance:

算法
================

.. automodule:: examples.algo
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: examples.algo.use_bisect
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: examples.algo.use_defaultdict
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: examples.algo.memoization
   :members:
   :undoc-members:
   :show-inheritance:


代码管理
================

API变化
---------------

sphinx标记 .. deprecated:: 1.1 ::

    .. deprecated:: 1.1

warnings 模块，warnings.warn()::

    warnings.warn("turn_left is deprecated sin Version 1.1, use trun instead")

debtcollector模块标注 ::

    from debtcollector import moves
    @move.moved_method("turn",version="1.1")

.. automodule:: examples.lang.api
   :members:
   :undoc-members:
   :show-inheritance:

文档
================

    文档::

        Sphinx
        http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

发布
================

    打包::

        历史
        推荐pbr
        wheel

测试
================

    单元测试


集成
===============


存储
===============

ORM
RMDB

NoSQL


优化
===============

.. automodule:: examples.profile.use_cprofile
   :members:
   :undoc-members:
   :show-inheritance: