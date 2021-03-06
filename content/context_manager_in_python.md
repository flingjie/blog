Title: Context manager in Python
Date: 2014-03-14 17:13:46
Category: Python

上下文管理器(context manager)是Python2.5开始支持的一种语法，用于处理指
定代码块进入和退出时的操作。一般使用with语法，也可以直接调用相应的方法。

**with语句**   
with语句是用来简化“try/finally”语句的，通常用于处理共享资源的获取和
释放，比如文件、数据库和线程资源。它的用法如下：

``` python
with VAR = EXPR:
    BLOCK
```
其相当于进行了如下操作：

``` python
VAR = EXPR
VAR.__enter__()
try:
    BLOCK
finally:
    VAR.__exit__()
```

例子如下：

``` python
import time
class demo:
    def __init__(self,label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print ('{}: {}'.format(self.label, end - self.start))

with demo('counting'):
    n = 10000000
    while n > 0:
        n -= 1;

#  counting: 0.933553934097

```

也可利用@contextmanager装饰器改写如下:

``` python
from contextlib import contextmanager
import time

@contextmanager
def demo(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

with demo('counting'):
    n = 10000000
    while n > 0:
        n -= 1
# counting: 0.947228908539

# 其中yield之前的所有代码都类似于__enter__方法的内容。而yield之后的所有
# 代码类似__exit__方法的内容。
```