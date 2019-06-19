#动态导入,导入的名字必须是字符串形式的
#动态导入是基于python的反射自省机制完成的

m1 = __import__('反射,自省')
# m1 = __import__('t1.c1.b1')  #m1为ti这个模块,但是默认运行t1.c1.b1


import importlib   #导入importlib
m2 = importlib.import_module('多态')
# m2 = importlib.import_module('t1.c1.b1') #  m2为b1,且默认运行








