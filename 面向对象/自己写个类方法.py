
class Foo:
    def __init__(self,func):
        self.func = func


    def __get__(self, instance, owner):
        def Wto(*args,**kwargs):       #在有其他参数的情况下,可以再嵌套个函数
            return self.func(owner,*args,**kwargs)
        return Wto


class People:
    def __init__(self,name):
        self.name = name

    @Foo
    def Life(cls,place):
        print('%s生活在%s上'%(cls.__name__,place))

People.Life('earth')
# print(People.__dict__)




# class People:
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def Life(cls,place):
#         print('%s生活在%s上'%(cls.__name__,place))
#
# People.Life('earth')






















