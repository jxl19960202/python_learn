#什么是析构函数,在python类内,析构函数用__del__表示(python是高级语言,解释器已经处理了内存),当程序执行完的时候运行析构函数,释放内存
class Foo:
    def __init__(self,name):
        self.name = name
    def __del__(self):        #程序执行完的时候运行
        print('---------')

f1 = Foo('jxl')
print(f1.name)
print('[[[[')
# del f1.name  #删除对象属性,触发的是__delatter__函数与__del__无关
del f1  #删除对象时也触发__del__函数,如果后面还有代码没运行完,执行后面的代码,__del__函数不执行
print('=====')


#什么是构造函数, 用__call__表示,将一个对象像一个函数一样使用
# def say():
#     print('-----')
# say()       #函数也是一个对象,函数的调用是调用了产生函数的类的__call__方法
#
# class Foo:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         return (args,kwargs)
# f1 = Foo()
# res = f1('jxl','age',**{'name':'星期天'})         #一个对象加括号,类似于函数的调用,调用该对象所在类内的__call__方法(一个对象加括号的形式)
# print(res)














