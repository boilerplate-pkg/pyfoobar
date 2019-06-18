
'''
术语
==========

reST
  reStructuredText, reST, standard reST markup

  语法手册：https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html

sphinx
  sphinx(http://sphinx-doc.org)

  Sphinx 在 standard reST markup 基础上新增了许多指令和文本解释角色

reST 标记 example
==================

* 星号: *text* 是强调 (斜体),
* 双星号: **text** 重点强调 (加粗),
* 反引号: ``text`` 代码样式.

章节::

 # 及上划线表示部分
 * 及上划线表示章节
 =, 小章节
 -, 子章节
 ^, 子章节的子章节
 ", 段落

sphinx 用法
============

sphinx-quickstart
doc/content.rst 
sphinx-build docs/ docs/build

http://www.sphinx-doc.org/en/stable/usage/quickstart.html

sphinx.ext.autodoc
https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

deps autodoc

automodule必须指明到模块
________________________

不能是上一级模块::

    .. automodule:: examples.use_sphinx
       :members:
       :undoc-members:
       :show-inheritance:

'''
