#继承:一个类继承一个或多个基类,可以通过该类调用基类内的属性,不用写重复代码
# class Humen:
#     start = 'erath'
#
# class People(Humen):
#     pass
#
# p1 = People()
# print(p1.start)


# 当子类与基类的属性重名时,该如何从子类中调用基类的属性

# class Vehicle:
#     def __init__(self,name,speed,energy):
#         self.name = name
#         self.apeed = speed
#         self.energy = energy
#     def run(self):
#         print('启动')
#
# class Ship(Vehicle):
#     def __init__(self,name,speed,energy,place,NNT):    #直接调用基类中的属性
#         self.nnt = NNT
#         self.place = place
#         Vehicle.__init__(self,name,speed,energy)
#     def run(self):
#         Vehicle.run(self)
#         print('船启动了')
#
#
# s1 = Ship('泰坦尼克号','60km/s','0il','大西洋',1000)
# s1.run()

#当基类的名字发生改变时,所有涉及到基类名的代码都要改变.采用super关键字使得改变代码量减少

class Vehicle1:
    def __init__(self,name,speed,energy):
        self.name = name
        self.apeed = speed
        self.energy = energy
    def run(self):
        print('启动')

class Ship(Vehicle1):
    def __init__(self,name,speed,energy,place,NNT):
        self.nnt = NNT
        self.place = place
        super().__init__(name,speed,energy)  #也可以是这种形式:super(Ship, self).__init__(name,speed,energy)

    def run(self):
        super().run()          #super().run() 的作用与 super(Ship, self).run()一样
        print('船启动了')


s1 = Ship('泰坦尼克号','60km/s','0il','大西洋',1000)
s1.run()


# class Vehicle1:
#     def __init__(self,name,speed,energy):
#         self.name = name
#         self.apeed = speed
#         self.energy = energy
#     def run(self):
#         print('启动')
#
# class Ship(Vehicle1):
#     pass
#
# s1 = Ship('泰坦尼克号','60km/s','0il')
# print(s1.name,s1.run())





