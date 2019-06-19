#设置一个people类,对people类输入的name,age,salary的类型进行限制name类型为str,age为int,salary为float


class _People:      #_People为一个描述符
    def __init__(self,n,genre):
        self.n = n
        self.genre = genre
    def __get__(self, instance, owner):  #   instance为被描述符描述的类的对象,owner为被描述符描述的类
        print('get',instance,owner)
        return instance.__dict__[self.n]

    def __set__(self, instance, value):
        print('set',instance,value)
        if not isinstance(value,self.genre):
            raise TypeError('%s输入的类型不是%s'%(self.n,self.genre))

        instance.__dict__[self.n] = value

    def __delete__(self, instance):
        print('delete',instance)
        instance.__dict__.pop(self.n)

class People:

    name = _People('name',str)     #类属性为一个描述符的对象
    age = _People('age',int)
    salary = _People('salary',float)
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

p1 = People('jxl',18,1000.0)       #这里没有强制规定,输入的参数是什么类型(现在要强制规定,输入的name为str,age为int,salary为float,不然就报错)




















