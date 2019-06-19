
#网络上传输的都是二进制数据
#tcp协议,是面向连接的传输协议.在建立链接前先启动服务器

from socket import *

addr = ('192.168.43.59',8008)
server = socket(AF_INET,SOCK_STREAM) #创建一个服务端对象.AF_INET是基于网络连接的,SOCK_STREAM相当于tcp协议
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #服务端可能会存在四次挥手的time_wait状态在占用地址,所以要重用ip和端口
server.bind(addr)  #将服务端绑定一个ip地址以及端口号
server.listen(5)  #这里指的是半链接池(相当于后台可以连接几个客户端,超出该数字的客户端连接不到,要排队)
                  #这里的服务器一次只能接受一位客户端,访问该服务器剩下的客户端会被放在一个半链接池中,等
                  #上一位完成后,在继续下一位
while True:
    coon,addr = server.accept()  #accept会接收客户端的2个参数,一个是s/c双向链接,一个是客户端的地址

    while True:
        try:                        #这里加入异常处理机制,当客户端中断连接不会报错
            date = coon.recv(1024)  #tcp是面向连接的,recv(内接一个字节(不一定))
        except Exception as e:
            print('发送错误')
            break
        print(date)
        coon.send(date.upper())  #给服务端返回一个发送来数据的大写



    coon.close() #关闭与该客户端的连接
server.close()  #关闭服务器







