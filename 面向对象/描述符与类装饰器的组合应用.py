class Humen:
    def __init__(self,n,genre):
        self.n = n
        self.genre = genre

    def __set__(self, instance, value):    #instance为被描述符描述的对象
        if not isinstance(value,self.genre):
            raise TypeError('%s输入的类型不是%s'%(self.n,self.genre))
        instance.__dict__[self.n] = value


    def __get__(self, instance, owner):
        instance.__dict__[self.n]

    def __delete__(self, instance):
        del instance.__dict__[self.n]


def Foo(**kwargs):
    def Too(obj):
        for key,value in kwargs.items():
            setattr(obj,key,Humen(key,value))
        return obj
    return Too


@Foo(name=str,age=int,salary=float)
class People:
    # name = Humen('name',str)
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
p1 = People('jxl',11,100000.0)
print(p1.__dict__)















