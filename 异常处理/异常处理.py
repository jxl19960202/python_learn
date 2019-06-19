#
#错误:1.语法错误 2.逻辑错误
#语法错误与异常处理无关
#什么是异常:异常是程序运行逻辑错误时发生的错误信息.分为3部分内容:异常类,异常值,异常的追踪信息
#异常处理是一种机制,程序运行错误时,设置异常处理接收异常,使得程序不会奔溃.一般常用 try...except...来处理异常(if判断也可以处理,只是麻烦)

#注意:将需要检验异常的代码放到try语句的代码块中
#举例:设置一个用户输入的salary,必须是浮点数形式的,否则会出错(且重新输入),检验用户输入的是否为float

#单分支
# while True:
#     try:
#         salary = input('salary:')       #一个异常标识一个异常类,当出现异常时,except该异常对应的类就可捕捉
#         res = float(salary)
#         print('--------')         #当try中的代码出现异常并被处理后,try中出现异常代码的后面的代码不会执行,跳出try语句
#         break
#     except ValueError as e:   #将异常值赋给e
#         print(e)
# print('=========')

#捕获所有异常的异常类   Exception
# while True:
#     try:
#         salary = input('salary:')       #一个异常标识一个异常类,当出现异常时,except该异常对应的类就可捕捉
#         res = float(salary)
#         print('--------')
#         break
#     except Exception as e:   #Exception类,捕获所有的异常(缺点:不知道出现哪个类型的异常)
#         print(e)
#
# print('=========')



#多分支,else(try子句下没有异常运行else下子句),finally(定义清理行为,及无论什么情况下都会执行)

try:
    salary = input('salary:')       #一个异常标识一个异常类,当出现异常时,except该异常对应的类就可捕捉
    res = float(salary)              #异常类有很多,但都继承BaseException异常类
    res1 = 1/0
    print('--------')

except ValueError as e:         #只捕捉ValueError的错误异常
    print(e)

except ZeroDivisionError as e:      #只捕捉ZeroDivisionError的错误异常
    print(e)

except Exception as e:        #Exception捕捉所有异常
    print(e)

else:                         #当try子句下的代码运行没有出错,就会运行else内的代码
    print('没有异常执行else')

finally:    #try 子句里面有没有发生异常，finally 子句都会执行。  如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
    print('有无异常都执行finally')    # 而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出。

print('=========')

























