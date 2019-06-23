
# 发布与安装

## 打包

历史:

    distutils, setuptools, distribute, distutils, distlib

推荐: 
    
    pbr, https://pypi.org/project/pbr/

## wheel

### 像jar包一样使用wheel包

``` bash
# package a wheel
python setup.py bdist_wheel

# run cmd line from wheel
python wheel-0.21.xxx.whl/wheel -h 

# another example
python foobar.zip
# eq
PYTHONPATH=foobar.zip python -m __main__

# another example
python foobar.zip/mymod
PYTHONPATH=foobar.zip python -m mymod.__main__
```

### 制作安装包

```
python setup.py bdist_wheel upload -r testpypi
```

## install

easy_install, Egg 缺少删除功能

### 实用pip

pip<https://pip.readthedocs.io/en/stable/user_guide>

``` python

# installpi
pip install numpy --timeout 60
pip install -i https://testpypi.python.org/pypi ceilometer
```

列出当前安装包

    pip freeze

## 发布 

``` python
setup.py sdist
python setup.py register -r testpypi
python setup.py sdist upload -r testpypi
```