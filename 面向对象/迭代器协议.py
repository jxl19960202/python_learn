# 迭代器是一个实现了迭代器协议的对象,那何为迭代器协议呢?(迭代器更节省内存)
# 满足下面两个条件就行。(1)该对象实现了__iter__()方法;(2)该对象实现了__next__()方法,返回当前
# 元素,并指向下一个元素的位置,如果当前位置已无元素,则抛出StopIteration异常。如果一个对象有__iter__()方法,那么它就是可迭代对象
#当迭代器迭代完之后,那么里面就什么数据都没有了.一个迭代器迭代到一个位置,下次迭代会从该位置开始,不会重头开始
#for循环:1.将一个可迭代对象变为迭代器,使用__iter__的方法 2.对该对象不断调用__next__方法.3.迭代完之后,进行异常处理,使程序不奔溃


# class Foo:
#     def __init__(self,x):
#         self.x = x
#     def __iter__(self):  #__iter__方法,将对象变为可以迭代
#         return self
#     def __next__(self):
#         if self.x >= 15:
#             raise StopIteration       #这是迭代完之后的终止异常
#         self.x += 1
#         return self.x
# f1 = Foo(8)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# for i in f1:               #for循环的机制,将可迭代对象变为迭代器(__iter__),不断调用__next__方法,最后接收终止异常
#     print(i)


#模拟range的加法:
# class Range:
#     def __init__(self,start,stop,step=1):
#         self.stop = stop
#         self.start = start
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         x = self.start
#         self.start += self.step
#         return x

# r1 = Range(1,7,3)
# for i in r1:
#     print(i)










