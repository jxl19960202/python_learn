#封装是一种思想,必须注意的是需要封装的属性才封装(否则的话,类会很乱),设计的时候要考虑清楚
#封装:顾名思义,就是将属性用东西装起来,且不让外部看到
#1.在class中把需要封装的属性钱加单下划线 _ ,这是一种约定,外部依然可以访问到
#2.在class中把需要封装的属性钱加双下划线 __ , 这是python机制自动将属性的名字变为 _类名__属性名.

# class People:
#     _start = 'earth'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1 = People('jxl',22)
# print(p1._start)   #只是约定

class People:
    __start = 'earth'
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = People('jx',22)
print(People.__dict__)
print(p1._People__start)  #python机制将加双下划线的属性名自动重命名,依然可以访问

#3.明确区分内外,内部的实现逻辑,外部无法知晓,并且为内部的实现逻辑提供外部的访问接口

# class People:
#     __start = 'earth'
#     def __init__(self,name,age):
#         self._name = name
#         self.age = age
#     def get_start(self):         #给外部访问提供接口
#         return self._name
# p1 = People('jxl',22)
# print(p1._name)











