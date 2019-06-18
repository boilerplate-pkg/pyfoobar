
'''
术语
==========

reST
  reStructuredText, reST, standard reST markup

  `语法手册 <https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html>`_
  `English Version <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

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

Link

This is a paragraph that contains `Baidu`_.

.. _Baidu: https://www.baidu.com/

Field lists (ref) are sequences of fields marked up like this::

  def my_function(my_arg, my_other_arg):
      """A function just for me.

      :param my_arg: The first of my arguments.
      :param my_other_arg: The second of my arguments.

      :returns: A message (just for me, of course).
      """  

    
.. todo::      

   blah
   blah


sphinx 用法
============

学习手册
https://my-study-restructuredtext.readthedocs.io/en/latest/

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
