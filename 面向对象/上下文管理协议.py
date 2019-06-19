#上下文管理协议 __enter__,__exit__
#用途或好处:使用with语句就是将代码块放在with中执行,with结束后自动完成清理工作
#在需要管理一些资源比如文件,网络连接和锁的编程,可以在__exit__中定制释放资源的机制.

class Foo:

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(exc_type)    #<class 'AttributeError'>   (出错所在的类)
        print(exc_val)     #'NoneType' object has no attribute 'name' (出错的内容)
        print(exc_tb)       #<traceback object at 0x000000DE2ABE0148>  (出错的追踪信息)
        return True

with Foo() as f:        #执行with就是在运行__enter__方法,将__enter__方法的返回值赋给f
    print(f)
    print(f.name)      #1.当代码块正常运行时,with下的代码块执行完之后再执行__exit__方法
    print('----')        #2.当代码块出错时,马上执行__exit__方法(exc_type,exc_type,exc_tb),然后终止程序
print('===')                         #2.1当代码块出错,但是__exit__方法内有返回值(return True(作用:相当于吞掉了错误)),
                          #在with下的出错代码处运行__exit__方法,with下的代码块出错代码后的代码不运行,运行with外的代码块













