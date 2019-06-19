#描述符 一个新式类具有__delete__,__set__,__get__函数中的至少1个,那这个类就是一个描述符(数据描述符具有__get__,__set__方法.非数据描述符没有__set__函数)
#一个新的类的类属性(数据属性,函数属性)是另一个描述符的类的实例化(该2个类必须是新式类)
#描述符的访问顺序:类属性->数据描述符->实例属性->非数据描述符
class Foo:
    def __set__(self, instance, value):
        print('__set__',instance,value)
        # instance.__dict__['x'] = value       #字典内添加属性
    def __get__(self, instance, owner):     #instance是被描述符描述的类的对象, owner是被描述符描述的类
        print('__get__')
    def __delete__(self, instance):
        print('__delete__')

class Boo:
    x = Foo()   #类属性x是Foo的实例化的对象,及是个描述符对象
    def __init__(self,x):
        pass
b1 = Boo(1)
# b1.x       #触发描述符类的__get__
# b1.x = 2   #(注意的是这里不会再在实例的__dict__添加x,而是触发描述符Foo中的触发描述符类的__set__)
# del b1.x     ##触发描述符类的__delete__
# Boo.x = 'woqu'        #类属性的替换操作(将描述符替换成'woqu')

#描述符__set__(self, instance, value),中instance, value是什么
# b1.x = 10 #触发描述符__set__,instance是<__main__.Boo object at 0x000000D63F273860>b1对象, value是10
# print(b1.__dict__)











