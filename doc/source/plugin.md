
# 入口点和插件

## ep

>> Entry points are a simple way for distributions to “advertise” Python objects (such as functions or classes) for use by other distributions.

### entry_point_inspector: 查看入口点信息

>> 通入规范的放口点描述，找到符合条件的模块函数

```
epi group list
epi group show gui_scripts
epi ep show gui_scripts spyder

```

### pkg_resources发现和加载入口点信息



## 建立插件机制

入口点机制提供了巨大的可能性，可以用来构建驱动系统，钩子系统以及简单而通用的扩展。

### stevedore

[stevedore](https://pypi.org/project/stevedore/)

>> Python makes loading code dynamically easy, allowing you to configure and extend your application by discovering and loading extensions (“plugins”) at runtime. Many applications implement their own library for doing this, using __import__ or importlib. stevedore avoids creating yet another extension mechanism by building on top of setuptools entry points. The code for managing entry points tends to be repetitive, though, so stevedore provides manager classes for implementing common patterns for using dynamically loaded extensions.


####  一个例子
学习Python动态扩展包stevedore
    
    http://yansu.org/2013/06/09/learn-python-stevedore-module-in-detail.html
