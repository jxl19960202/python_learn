#程序运行出现异常,会报出一个异常类.那么自己也可以定义一个异常类

class LazyError(BaseException):  #自己创建一个异常类,该类要继承BaseException
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

# raise TypeError('wrong')     #使用raise语句主动触发异常, TypeError('wrong')相当于该异常类实例化.触发了该异常(程序终止)

try:
    raise LazyError('wrong')     #raise 主动触发的异常可用异常处理机制处理
except LazyError as e:
    print(e,'------')
print('=====')











