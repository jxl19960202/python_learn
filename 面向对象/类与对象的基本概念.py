#类与对象的概念
#类指的是一类事物的共性整合到一起,对象指的是具有该共性的一种事物.如藏獒与狗类,北大与学校,抽象与具体的

# 类中具有数据属性与函数属性,对象没有函数属性,调用的是类的
# class Dog:  #类的命名:一般情况下首子母大写
#     '''
#     这是一个狗类    #文档
#     '''
#     name = 'alex'  #这是类变量
#     def jiao():          #函数属性
#         print('大声点叫啊')
# # print(Dog.__dict__)     #__dict__以字典的形式查看类中的属性(也适用于对象等)
# Dog.__dict__['jiao']()
# Dog.jiao()  #点号的调用实际上是调用了类中的__dict__的索引

# class Dog:
#     def __init__(self,name,age):  #__init__ 函数表示初始化
#         self.name = name
#         self.age = age            #对象只有数据属性,函数属性调用的都是类的
#     def jiao(self):
#         print('%s 在叫' %(self.name))
#
# d1 = Dog('旺财',18)  #这是类的事例化,实例成具体的d1
# print(d1.__dict__)
# # print(d1.__dict__)   #self 在这里指的是d1
# d1.jiao()    #d1的__dict__中没有jiao()数据,为什么能调用呢(解:调用的是Dog这个类中的jiao()属性)

#类,实例特性的增删改查   类似于字典的增删改查
#类,实例的增删改查,是对其内的属性字典进行操作,可以通过__dict__方法查看
class People:
    mingzhu = '汉'  #类变量
    def __init__(self,name,age):
        self.name = name   #实例变量
        self.age = age

People.mingzhu = '满'  #改变类变量
print(People.mingzhu)
del People.mingzhu    #删除类变量

p1 = People('jxl',18)

p1.name = 'jrj'   #改变实例变量   ,删除与类变量删除方法类似, del
p1.gender = 'man'  #为p1对象添加属性
print(p1.name,p1.age,p1.gender,p1.__dict__)  #查看












