#多态:多态来源于继承(有继承才会有多态),是指不同的对象调用相同的方法(函数)
#1.
# a = [1,2,3,4,5]
# b = 'abcde'
# res1 = len(a)
# res3 = a.__len__()       #a,b调用了len函数也是一种多态的体现,调用len函数实际上是调用了对象的__len__()
# res2 = len(b)
# res4 = b.__len__()
# print(res1,res2)
# print(res3,res4)

#2.
# class Animal:
#     def action(self):
#         print('活动')
#
# class Cat(Animal):
#     pass
# class Dog(Animal):
#     pass
#
# c1 = Cat()
# c1.action()
# d1 = Dog()    #不同的对象调用了相同的方法,基于继承的特性
# d1.action()
# def action(obj):      #将obj.action()函数定义了一个新的函数
#     return obj.action()
# action(c1)


















