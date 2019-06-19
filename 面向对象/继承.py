#继承  子类继承基类的属性(只是调用,不会加载到子类的__dict__中)
#继承  继承和派生(衍生新的属性)
# class Animal:
#     def action(self):
#         print('动')
#     def eat(self):
#         print('吃')
#     def sleep(self):
#         print('睡')
#
# class Cat(Animal):
#     def __init__(self,name):
#         self.name = name
#     def mew(self):           #派生,继承基类的所有属性,衍生自己的mew属性
#         print('喵喵喵')
#
# class Dog(Animal):
#     def __init__(self,name):
#         self.name = name
#     def bark(self):
#         print('汪汪汪')
#     def sleep(self):
#         print('没睡')
#
# c1 = Cat('小猫')
# c1.action()
# c1.mew()
# d1 = Dog('小狗')
# d1.action()
# d1.bark()
# c1.sleep()
# d1.sleep()  #当子类总的属性与基类重名时,调用子类的属性(基类的属性不变)


#接口继承     归一化设计(类似一切皆文件)
import abc                            #python中没有强制规定接口继承,调用abc模块
class Animal(metaclass=abc.ABCMeta):

    @abc.abstractmethod           #对需要设定的接口加上装饰器
    def action(self):
        pass

    @abc.abstractmethod
    def eat(self):              #提供了3个接口(action,eat,sleep),不用具体实现
        pass

    @abc.abstractmethod
    def sleep(self):
        pass                        #对于基类中加了@abc.abstractmethod装饰器的接口,子类必须实现
                                    #不然会报错

class Dog(Animal):
    def action(self):
        print('action')

    def sleep(self):
        print('sleep')

    def eat(self):
        print('eat')

    def papa(self):
        print('papa')

d1 = Dog()










