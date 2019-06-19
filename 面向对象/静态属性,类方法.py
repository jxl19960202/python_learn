#静态属性  作用:

# class Room:
#     def __init__(self,high,weigh,long):
#         self.high = high
#         self.weigh = weigh
#         self.long = long
#
#     @property         #静态属性的装饰器  函数属性类似于转变成数据属性
#     def mianji(self):
#         return self.long * self.weigh
#
# r1 = Room(10,10,10)
# print(r1.mianji)
# r2 = Room(1,2,1)
# print(r2.mianji)

#类方法 :只是类级别的操作

# class People:
#     place = 'earth'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def behavior(cls):   #cls 指的是将这个类People
#         return '人类是用两条腿走路的'
#
# print(People.behavior())








