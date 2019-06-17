
# install

## linux

pip install pyltp

## windows

```
 $ git clone https://github.com/HIT-SCIR/pyltp
 $ cd pyltp
 $ git submodule init
 $ git submodule update
 $ python setup.py install # Mac系统出现版本问题使用 MACOSX_DEPLOYMENT_TARGET=10.7 python setup.py install
```

```
python setup.py bdist_wheel
```

```
pip install pyltp-0.2.1-cp37-cp37m-win_amd64.whl
```

# data


ltp_data_v3.4.0
http://ltp.ai/download.html