#只要记住 @装饰器 就相当于 obj = 装饰器(obj)  这里的obj为被装饰的类

#第一种:
# def Foo(obj):   #装饰器:在函数的参数里传入一个对象,(可以在这个函数里调用该对象或者是返回值为该对象)
#     print('Foo',obj)
#     return obj
#
# @Foo      #相当于L = Foo(L)
# class L:
#     pass
# # L()

#第二种
# def Foo(obj):
#     def two(*args,**kwargs):
#         print(args,obj)
#         return obj
#     return two
# #
# @Foo  #a = Foo(a) --->a = two
# class a:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a1 = a('jxl',18)  #a('jxl',18) --->two('jxl',18)---
# print(a1.__dict__)
#第三种
# def Foo(*args,**kwargs):
#     def Two(obj):
#         print(kwargs,obj)
#         return obj
#     return Two
#
# @Foo(x=1,y=2) #1.Foo(x=1,y=2) = Two 2.@Two -->Z = Two(Z) 运行Two函数,并返回Z
# class Z:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# Z(1,2)









#类的装饰器与描述符组合应用
# class _People:      #_People为一个描述符
#     def __init__(self,n,genre):
#         self.n = n
#         self.genre = genre
#     def __get__(self, instance, owner):  #   instance为被描述符描述的类的对象,owner为被描述符描述的类
#         # print('get',instance,owner)
#         return instance.__dict__[self.n]
#
#     def __set__(self, instance, value):
#         # print('set',instance,value)
#         if not isinstance(value,self.genre):
#             raise TypeError('%s输入的类型不是%s'%(self.n,self.genre))
#
#         instance.__dict__[self.n] = value
#
#     def __delete__(self, instance):
#         # print('delete',instance)
#         instance.__dict__.pop(self.n)
#
# def Foo(**kwargs):
#     def Too(ojb):
#         for n,genre in kwargs.items():
#             setattr(ojb,n,_People(n,genre))
#         return ojb
#     return Too
#
#
#
# @Foo(name=str,age=float,salary=float)    #先运行Foo(name=str,age=float,salary=float)得到Too,@Too就是People = Too(People)
# class People:
#     def __init__(self,name,age,salary):  #加类的装饰器,作用是:给People加了3个类属性
#         self.name = name                 # 1.'name'= <__main__._People object at 0x000000B132143DA0> 描述符对象
#         self.age = age                   #2. 'age'= <__main__._People object at 0x000000B1321E8A20>
#         self.salary = salary              #3. 'salary'= <__main__._People object at 0x000000B1321E8A90>
# # p1 = People('jxl',10.0,1000.0)
# print(People.__dict__)



# user_list=[
#     {'name':'alex','passwd':'123'},
#     {'name':'linhaifeng','passwd':'123'},
#     {'name':'wupeiqi','passwd':'123'},
#     {'name':'yuanhao','passwd':'123'},
# ]
#
# current_user={'username':None,'login':False}
#
# def auth_deco(func):
#     def wrapper(*args,**kwargs):
#         if current_user['username'] and current_user['login']:
#             res=func(*args,**kwargs)
#             return res
#         username=input('用户名: ').strip()
#         passwd=input('密码: ').strip()
#
#         for index,user_dic in enumerate(user_list):
#             if username == user_dic['name'] and passwd == user_dic['passwd']:
#                 current_user['username']=username
#
#                 current_user['login']=True
#                 res=func(*args,**kwargs)
#                 return res
#                 break
#         else:
#             print('用户名或者密码错误,重新登录')
#
#     return wrapper
#
# @auth_deco   #index=auth_deco(index)=wrapper
# def index():
#     print('欢迎来到主页面')
#
# @auth_deco
# def home():
#     print('这里是你家')
#
# def shopping_car():
#     print('查看购物车啊亲')
#
# def order():
#     print('查看订单啊亲')
#
#
# print(index())  #wrapper()
#
# home()


# user_list=[
#     {'name':'alex','passwd':'123'},
#     {'name':'linhaifeng','passwd':'123'},
#     {'name':'wupeiqi','passwd':'123'},
#     {'name':'yuanhao','passwd':'123'},
# ]
#
# current_user={'username':None,'login':False}
# def auth(auth_type='file'):
#     def auth_deco(func):
#         def wrapper(*args,**kwargs):
#             if auth_type == 'file':
#                 if current_user['username'] and current_user['login']:
#                     res=func(*args,**kwargs)
#                     return res
#                 username=input('用户名: ').strip()
#                 passwd=input('密码: ').strip()
#
#                 for index,user_dic in enumerate(user_list):
#                     if username == user_dic['name'] and passwd == user_dic['passwd']:
#                         current_user['username']=username
#                         current_user['login']=True
#                         res=func(*args,**kwargs)
#                         return res
#                         break
#                 else:
#                     print('用户名或者密码错误,重新登录')
#             elif auth_type == 'ldap':
#                 print('巴拉巴拉小魔仙')
#                 res=func(*args,**kwargs)
#                 return res
#         return wrapper
#     return auth_deco


#auth(auth_type='file')就是在运行一个函数,然后返回auth_deco,所以@auth(auth_type='file')
#就相当于@auth_deco,只不过现在,我们的auth_deco作为一个闭包的应用,外层的包auth给它留了一个auth_type='file'参数
# @auth(auth_type='file')  #-->@auth_deco -->index=auth_deco(index)=wrapper -->index()相当于wrapper()
# def index():
#     print('欢迎来到主页面')
#
# @auth(auth_type='ldap')
# def home():
#     print('这里是你家')
#
# def shopping_car():
#     print('查看购物车啊亲')
#
# @auth(auth_type='file')
# def order():
#     print('查看订单啊亲')
#
#
# index()
# print(current_user)
# order()


# class a:
#     def __init__(self,a):
#         self.a = a
#     def a1(self):
#         if self.a == 1:
#             print('fuck')
#
# class b(a):
#     pass
#
# b = b(1)
# b.a1()

# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('函数[%s],运行时间是[%s]' %(func,stop_time-start_time))
#         return res
#     return wrapper
#
#
# @timer  #@timer就等同于cal=timer(cal)=wrapper
# def cal(array):
#     res=0
#     for i in array:
#         res+=i
#     return res
#
# print(cal(range(100000))) #-->wrapper(range(1000)) -->res=cal(range(1000))


class animal:

        print('run')

class cat(animal):
    def __init__(self,name):
        self.name = name
        print(name)

c1 = cat('ll')



















