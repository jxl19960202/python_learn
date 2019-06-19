#说明一点,print函数实际上是触发了__str__()函数,类内部的__str__默认函数
class Aoo:
    pass

a1 = Aoo()              #这2者同样是实例话,输出结果不一样,这是由类内的__str__不同所导致的
l = list('mn')  #l可以看做是由list类实例化而来的对象
print(a1,l)  #那么打印结果为什么不一样呢




# class Foo:
#     def __str__(self):
#         return '这是Foo的实例'
#
# f1 = Foo()     #这里改写了类内的__str__函数,print输出结果就变了(print输出结果必须是str格式)
# print(f1)



# __str__与__repr__区别,前者是在编译器中运行的,后者在终端中运行







