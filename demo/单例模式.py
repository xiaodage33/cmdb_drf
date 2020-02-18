import time
import threading
class Singleton(object):
    instance = None # 静态字段、类变量
    lock = threading.RLock()
    def __init__(self,name):
        """初始化对象"""
        self.name = name

    def __new__(cls, *args, **kwargs):
        """创建对象"""
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                time.sleep(0.2)
                cls.instance = object.__new__(cls)
            return cls.instance


def func():
    obj = Singleton('xx')
    print(obj)

for i in range(10):
    t= threading.Thread(target=func)
    t.start()

time.sleep(60)

obj = Singleton('xx')