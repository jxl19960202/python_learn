#类也可以作为装饰器

# class LazyProperty:
#     def __init__(self,func):
#         self.func = func       #这里的 self.func 为Sum类中的Total
#
#     def __get__(self, instance, owner):
#         if not instance:
#             return self.func
#         res = self.func(instance)
#         print(instance)
#         setattr(instance,self.func.__name__,res)   #这一步,将总价Total与计算结果写到s1的实例中
#         return res                                #func.__name__,表示该函数的函数名
#
# class Sum:
#     def __init__(self,name,num,price):
#         self.name = name
#         self.num = num
#         self.price = price
#
#     @LazyProperty   #Total = LazyProperty(Total) --->触发LazyProperty的__init__方法
#     def Total(self):
#         return self.num*self.price
#
#
#
# s1 = Sum('apple',10,5.5)
# print(s1.Total,'-----',s1.__dict__)  #-->s1.Total触发装饰器的__get__方法



class LazyProperty:
    def __init__(self,func):
        self.func = func       #这里的 self.func 为Sum类中的Total

    def __get__(self, instance, owner):
        print(instance,owner)
        if not instance:               #当用类调用Total,及没有对象 instance为None
            return self.func
        res = self.func(instance)
        setattr(instance,self.func.__name__,res)   #这一步,将总价Total与计算结果写到s1的实例中
        return res                                #func.__name__,表示该函数的函数名

class Sum:
    def __init__(self,name,num,price):
        self.name = name
        self.num = num
        self.price = price

    @LazyProperty   #Total = LazyProperty(Total) --->触发LazyProperty的__init__方法
    def Total(self):
        return self.num*self.price




s1 = Sum('apple',10,5.5)
print(s1.Total)



#property,静态属性的增删改查


# class Animal:
#
#     @property
#     def action(self):
#         return 'action'
#
#     @action.setter
#     def action(self,value):
#         print(value)
#         return 'action'
#
#     @action.deleter
#     def action(self):
#         return 'action'
#
# a1 = Animal()
# a1.action = 'set'
# print(a1.action)
# del a1.action
# print(a1.action)









