# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；可以用next（）方法持续调用，直到报错。
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不能用next（）方法，不过可以通过iter()函数(调用__iter__()方法)获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的 比如：for循环一个列表（1.将列表变为terator 2.持续调用next（），并且补获了异常）
# a = 'abc'
# print(type(a))   #<class 'str'> 不具有next（）
# a = iter(a)
# print(type(a)) #<class 'str'>   具有next（）
#
# 三元表达式
# x = int(input('输入'))
# print(1) if x>5 else print(0)
# 列表解析式
# a = [i for i in range(10)]   #生成0到10的列表,还可以在后面加条件判断
# a = [i for i in range(10) if i >5]
# 也可以传入2个元素
# dict1 = {'a':1,'b':1,'c':1,'d':1,}
# a1 = [(v,m) for v,m in dict1.items()]
# print(a1)
# for v,m in dict1.items():
#     print(v,m)
#
#
# 生成器:列表生成器,函数式生成器
# 列表解析式变为列表生成器,将[]改为().列表解析式在内存中保存的是列表,生成器保存的是算法(更节省内存)
# a = ( i for i in range(10) if i >5)
# print(a)                               #生成器的特点1: 生成器只能迭代一次,迭代完了就没了.
# for i in a:                             #特点2:状态挂起 当上一次计算完之后,保留状态,下一次计算从上一次计算之后开始
#     print(i)
# print(a.__next__())
#
# 函数生成器   可以用next()调用   python语法规定:函数内有yield关键字,该函数就为函数式生成器
# def _print():
#     yield 1              #  yield,函数调用运行遇到yield停止,将yield的值返还给函数(类似与return)
#     yield 2              #当继续调用函数的next()时,函数从上一次的yield开始,到下一次的yield结束
#     yield 3
# a = _print()
# print(type(a),a.__next__())      #<class 'generator'>   1
#
# 可以用for循环调用yield
# def _num2():
#     for i in range(5):
#         yield '当前数字是%s'%str(i)
# a1 = _num2()     #a1为<class 'generator'>类
# print(a.__next__())
# print(a.__next__())
# a2 = _num2()
# for i in a2:       #也可以用for循环,迭代函数生成器
#     print(i)
#
# seed(value)
# def _num2():
#     for i in range(5):
#         _send = yield '当前数字是%s'%str(i)
#         print(_send)
# a1 = _num2()
# print(a1.__next__())
# print(a1.send(None))   #send()方法相当于操作了一次__next__,不同的是将send(value)中的value传给了上一次yield的赋值(该例子中的_send)
# print(a1.send('10'))    #当seed前没有运行过__next__,seed(value)中的value必须为None,否者会报错
#
# 模拟单线程的并发:并发(几个程序同时运行)
# 模拟买卖烤饼
# import time
# def buy(name):
#     while True:
#         time.sleep(0.5)
#         baozi = yield
#         print('%s买包子%s'%(name,baozi))
#
# def product(num,*args):
#     for j in args:
#         j_buy = buy(j)
#         j_buy.__next__()
#         for i in range(1,num+1):
#             j_buy.send('第%s只'%i)
# product(5,'jiang','xiao','long')













