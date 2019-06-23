# 文档规范

## 使用sphinx

    http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html


## 使用Sphinx解析markdown

> This is my answer, taken from [StackOverflow](http://stackoverflow.com/a/33797841/322283)

> [example](https://github.com/serra/sphinx-with-markdown)

You can use Markdown and reStructuredText in the same Sphinx project. How to do this is succinctly documented on [Read The Docs]. Install recommonmark (`pip install recommonmark`) and then edit `conf.py`:

    from recommonmark.parser import CommonMarkParser
    
    source_parsers = {
        '.md': CommonMarkParser,
    }
    
    source_suffix = ['.rst', '.md']

 [Read The Docs]: http://docs.readthedocs.org/en/latest/getting_started.html#in-markdown
 [beni]: http://stackoverflow.com/a/2487862/322283

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

