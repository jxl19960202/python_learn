#isinstance 判断一个对象是不是有另一个类(包括该类的所有上级)产生的
# class Foo:
#     pass
#
# class Doo(Foo):
#     pass
#
# d1 = Doo()
# print(isinstance(d1,Doo),isinstance(d1,Foo))


# issubclass() 用于判断一个类是否继承另一个类
# class Foo:
#     pass
#
# class Doo(Foo):
#     pass
#
# d1 = Doo()
# print(issubclass(Doo,Foo))


res = isinstance('name',(int,float,str))  #表面该属性只要是括号内类的一种就ok了
print(res)   #返回值为True



