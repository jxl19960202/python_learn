#对象是通过一个class类的实例化而来,一切皆对象,class本质上也是对象,那么class是怎么来的呢?
#class类是通过python的内建元类type实例化而来.
#元类 == metaclass
#一个类如果没有申明自己的元类,默认他的元类为type.还可以通过继承type来自定义元类
#通过type建立一个类,类 = type(object_or_name, bases, dict) 这3个参数分别为1.建立的类名 2.该类所继承的类(元组)(一般为object).3.该类的属性(数据属性,方法)

# def text(self):
#     print('text')
#
# Humen = type('People',(object,),{'age':18,text.__name__:text}) #继承的类要写成元组形式,可能继承多个类
# print(Humen,Humen.__dict__)
#
# t1 = Humen()
# t1.text()



class Humen(type):
    def __init__(self,name,bases,dict):    #这里的self为People类
        print(self)     #<class '__main__.People'>
        print(name)      #People 类名 由元类实例化得到的类名
        print(bases)      #(<class '__main__.foo'>,),People继承的类(可能继承的是多个类,由元祖形式表示)
        print(dict)       #People类的__dict__属性
    def __call__(self, *args, **kwargs):
        print('call',self,args,kwargs)
        res = object.__new__(People)   #调用object类的__new__方法,并传入参数(People类),获得的是People类的一个对象
        res.__init__(*args,**kwargs)
        return res

class foo:
    pass

class People(foo,metaclass=Humen):     #metaclass=Humen 就是 People = Humen(People),运行元类(Humen)的__init__方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        return 'hello'

p1 = People('JXL',18)      #这里的People相当于是由Humen元类产生的对象, People()相当于运行了元类Humen的__call__方法:,并将__call__方法的返回值给p1
p2 = Humen.__call__(People,'jxl',17) #及 p1 = People('JXL',18) 就是 p1 = Humen.__call__(People,'JXL',18),作用相同


































