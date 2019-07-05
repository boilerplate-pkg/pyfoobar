
# 开发环境与工具

## reference

https://github.com/jobbole/awesome-python-cn



## 虚拟环境

### virtual env

```python
virtualenv venv --system-site-package
```

### pip

config
windows:  C:\Users\tony\AppData\Roaming\pip\pip.ini
```
[global]
timeout = 60
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org
               pypi.tuna.tsinghua.edu.cn
```

## vscode

### config for windows

``` json
{
    "cmake-tools-helper.cmake_download_path": "c:\\Users\\tony\\.vscode\\extensions\\maddouri.cmake-tools-helper-0.2.1\\cmake_download",
    "workbench.startupEditor": "newUntitledFile",
    "workbench.colorTheme": "Electron Highlighter",
    "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\cmd.exe",
    "terminal.integrated.shellArgs.windows" : ["/K", "C:\\Users\\tony\\Anaconda3\\Scripts\\activate.bat", "C:\\Users\\tony\\Anaconda3"],
    "git.enableSmartCommit": true,
    "git.autofetch": true,
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "python.jediEnabled": false
}
```

## lint

## print

```python
from pprint import pprint
```

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
