#反射,自省  作用:可实现可插拔机制
#hasattr(对象或类,字符串新式的属性),getattr(),delattr(),setattr() 增删改查,这4个函数也适用于类(类在python中也是对象)
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = People('jxl',22)

res = hasattr(p1,'name')   #判断p1对象中有无'name'属性,返回bool值
print(res)


res2 = getattr(p1,'name','kong')  #作用与p1.name相同,当p1中不存在name属性时,报错或者是返回default的值
print(res2)                      #getatter查看

delattr(p1,'name')  #删除操作,类型与 del p1.name
# del p1.name      #del删除,实际上是调用了类内的内置函数__delatter__(默认运行的)
print(p1.__dict__)

setattr(p1,'gender','man')  #添加改动操作,类似于 p1.start = 'earth'
print(p1.__dict__)         #setatter添加改动,实际上是调用了类内的内置函数__setatter__(默认运行的)

if hasattr(p1,'name'): #实现可插拔机制
    pass                #判断一个逻辑完成没,完成了进行一段逻辑,没完成进行另一段逻辑
else:
    print('其他逻辑')


# class People:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __getattr__(self, item):      #__getattr__函数,在对象,类中无法找到属性时,触发__getattr__函数
#         pass
#     def __delattr__(self, item):
#         self.__dict__.pop(item)
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value   #这里不能写成self.key = value(会陷入无限递归,不断触发__setattr__函数)
#
# p1 = People('jxl',22)   #实例化时会运行__setattr__函数,增加改动也会触发
#
# res = getattr(p1,'name')
# print(res)






























