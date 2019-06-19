# def funct(x,y = None):
#     print(x,end='-')
#     print(y)
#
# funct1 = funct(3)
# funct2 = funct(3,4)

# def funct(x,y ):
#     print(x,end='-')
#     print(y)
#
# funct1 = funct(x = 3,y = 4)
# funct2 = funct(y = 4,x = 3)

# def funct(x,**kwarges):
#     print(x,end=' & ')
#     print(kwarges)
# funct(1,a=1,b=3)
# funct(2,**{'a':1,'b':3})
# funct(1)

# def funct(*arges,**kwarges):
#     print(arges,end=' & ')
#     print(kwarges)
# funct(1,a=1,b=3)
# funct(2,**{'a':1,'b':3})
# funct(1)
#函数，嵌套函数，函数内的变量私有化，全局变量与局部变量
#函数既变量，变量的访问顺序，global，nonlocal关键字
# name = 'jxl'
# def _name():
#     print(id(name),name)
# _name()
# print(id(name),name)

# name = 'jxl'
# def _name():
#     global name
#     name = 1
#     print(id(name),name)
# _name()
# print(id(name),name)

# NAME = ["产品经理","廖波湿"]
# def qupengfei():
#
#     NAME.append('天扎龙')
#     print('我要搞', NAME)
#
# qupengfei()

# name = '干娘'
# def weihou():
#     name = "陈卓"
#     def weiweihou():
#         nonlocal name   # nonlocal，指定上一级变量，如果没有就继续往上直到找到为止
#         name = "冷静"
#         print(id(name))
#
#     weiweihou()
#     print(id(name))
#     print(name)
#
# print(name)
# weihou()
# print(name)

# def bar():
#     print('from bar')
# def foo():
#     print('from foo')
#     bar()
#
# foo()

# def _print():
#     print('jxl')
#     def _print1():
#         print('jjt')
#     _print1()
#
# _print()








