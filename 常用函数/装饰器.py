# 什么是装饰器. 装饰器是一个函数(高阶函数,嵌套函数,闭包),
# 作用:装饰器就是装饰函数的,及给函数添加功能
# 原则:1.不改变被装饰的函数的内部代码 2.不改变被装饰函数的调用方式
# 高阶函数(1.函数接收的参数是一个函数名 2.函数的返回值是一个函数名)
# def too():
#     print('from too')
# def foo():
#     print('from foo')
#     return too
# a = foo()
# a()
#
# def too():
#     print('from too')
# def foo(func):
#     print('from foo')
#     func()
# a = foo(too)
#
# 函数嵌套 定义一个函数,在该函数的代码块中在定义函数
# def foo():
#     print('from in foo')
#     def too():
#         print('from in too')
#     return too
# too = foo()
# too()
#
#
# 闭包,将变量用函数封装起来
# def foo():
#     def woo():
#         print('闭包')
#     return woo
# woo = foo()
# woo()

# 装饰器:
# 给一个函数加一个测试函数调用时间的装饰器
import time
def foo(func):
    def Two(*args,**kwargs):
        a = time.time()
        res = func(*args,**kwargs)
        b = time.time()
        print(b - a)
        return res
    return Two

#
# @foo   #语法规定,@foo等同与two = foo(two).作用是在给不同的函数加装饰器时,只要在函数的前
# 面加上@装饰器的函数名就可以了.不需要给函数添加功能的就不需要加.(同时,还可以给函数加多个装饰器)
# 运行加了装饰器的函数,实质上是在运行装饰器(把函数放在装饰器内部运行)
@foo
def two(name,age):
    time.sleep(1)
    print('我叫%s,今年%s岁'%(name,age))
    return '不错'
two = foo(two)
res1 = two('jiang','18')


# 装饰器的练习(模拟多个页面,判断用户名,密码(正确执行))
# dict1 = {'jiang':'123','xiao':'234','long':'456'}
# flag = False #作用是避免重复输入(当输入一次正确的结果时,以后的就不用输入了)
# def solution(func):  #判断用户输入,正确及执行
#     def swarrp():
#         global flag
#         if flag:
#             res = func()
#             return res
#         else:
#             username = input('请输入用户名:')
#             usercord = input('情输入密码:')
#             if username in dict1 and usercord == dict1[username]:
#                 res = func()
#                 flag = True
#                 return res
#             else:
#                 print('输入错误')
#     return swarrp
#
# @solution
# def _main():
#     print('欢迎来到主页面')
# _main()
#
# @solution
# def _second():
#     print('欢迎来到次页面')
# _second()
#
# @solution
# def _ShopCar():
#     print('快来清空购物车啊')
# _ShopCar()















