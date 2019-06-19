#调用类,对象中的属性时是采用点号 . (及从__dict__中调用的)
#对象以点号的形式调用属性,先从对象的属性字典内查找,找不到,会去类的属性字典内找(包括继承的类),在找不到就报错
#1.
# hu = 'america'
# # class humen:
# #     hu = 'chinese'
# #     def __init__(self,hu):
# #         self.hu = hu
# #
# # h1 = humen('jepan')
# # print(h1.hu)

#2.
# hu = 'america'
# class humen:
#     hu = 'chinese'
#
# h1 = humen()
# print(h1.hu)

# 3.
hu = 'america'
class humen:
    hu = 'chinese'
    def __init__(self):
        print(hu)      #这里是直接调用hu属性,与类,实例的属性字典无关,直接调用的是全局变量

h1 = humen()
