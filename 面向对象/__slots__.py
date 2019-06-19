#__slots__ 在类内设置__slots__属性,实例化后的对象就不会有__dict__属性.(减少内存的消耗,以及更快的访问速度)
#
class Foo:
    __slots__ = ['name','age']#可以是一个属性,也可以是多个属性(数组的形式组合)
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print('sb')

f1 = Foo('jxl',18)
print(f1.__slots__,Foo.__slots__,f1.name)

# del f1.name
# f1.gender = 'man'  #只能设置或者更改__solts__数组内的属性,设置其他的会报错
Foo.__dict__   #在设置__slots__属性时,对象没有__dict__属性,类是具有的













