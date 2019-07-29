# 开发库支持(net.Scrapy)

## Scrapy shell

testing XPath or CSS expressions

scrapy.cfg:
``` 
[settings]
shell = bpython
```

中断，并进入到调试模式
``` python
from scrapy.shell import inspect_response
inspect_response(response, self)
```

调试插件
https://docs.scrapy.org/en/latest/topics/extensions.html#debugger-extension
```python
class scrapy.extensions.debug.Debugger
Invokes a Python debugger inside a running Scrapy process when a SIGUSR2 signal is received. After the debugger is exited, the Scrapy process continues running normally.
```

## Other

### ScreenShot
[Splash - A javascript rendering service](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#take-screenshot-of-item)
Splash is a javascript rendering service. It’s a lightweight web browser with an HTTP API, implemented in Python 3 using Twisted and QT5. The (twisted) QT reactor is used to make the service fully asynchronous allowing to take advantage of webkit concurrency via QT main loop. 