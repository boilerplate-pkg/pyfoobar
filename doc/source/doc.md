# 文档规范

## 使用sphinx

    http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html


## 使用Sphinx解析markdown

> This is my answer, taken from [StackOverflow](http://stackoverflow.com/a/33797841/322283)

> [example](https://github.com/serra/sphinx-with-markdown)

> [document](https://recommonmark.readthedocs.io)

You can use Markdown and reStructuredText in the same Sphinx project. How to do this is succinctly documented on [Read The Docs]. Install recommonmark (`pip install recommonmark`) and then edit `conf.py`:

    from recommonmark.parser import CommonMarkParser
    
    source_parsers = {
        '.md': CommonMarkParser,
    }
    
    source_suffix = ['.rst', '.md']

 [Read The Docs]: http://docs.readthedocs.org/en/latest/getting_started.html#in-markdown
 [beni]: http://stackoverflow.com/a/2487862/322283
 
## markdown 内嵌rst

```eval_rst
.. autoclass:: recommonmark.transform.AutoStructify
    :show-inheritance:
```

实现方法
```python
import recommonmark.transform
github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(recommonmark.transform.AutoStructify)
```

``` python
### ```eval_rst
### .. autoclass:: recommonmark.transform.AutoStructify
###    :show-inheritance:
### ```
```

还可以引用其他文档

* [Lang](lang.md)
* [Libs](libs.md)
* [Algo](algo.md)

### 一个高级例子

``` sidebar:: Line numbers and highlights

     emphasis-lines:
       highlights the lines.
     linenos:
       shows the line numbers as well.
     caption:
       shown at the top of the code block.
     name:
       may be referenced with `:ref:` later.
```

``` code-block:: python
     :linenos:
     :emphasize-lines: 3,5
     :caption: An example code-block with everything turned on.
     :name: Full code-block example

     # Comment line
     import System
     System.run_emphasis_line
     # Long lines in code blocks create a auto horizontal scrollbar
     System.exit!
```

## rst, reST, reStructuredText, reST, standard reST markup

语法手册

    https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html

English Version

    http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

学习手册

    https://my-study-restructuredtext.readthedocs.io/en/latest/
    http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

sphinx-quickstart

    doc/content.rst 
    sphinx-build docs/ docs/build
    http://www.sphinx-doc.org/en/stable/usage/quickstart.html

sphinx.ext.autodoc

    https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

