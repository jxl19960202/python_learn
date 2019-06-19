#udp不是面向连接的,支持多个客服端连接服务端(并发)
#udp不需要建立双向链接,先启动哪一端都不会报错

from socket import *
ip_port =('192.168.43.59',8008)
size = 1024
udp_server = socket(AF_INET,SOCK_DGRAM) #SOCK_DGRAM是基于udp协议数据报类型的,
udp_server.bind(ip_port)   #绑定ip,端口号
while True:
    try:
        date,addr = udp_server.recvfrom(size) #recvfrom(),接收2个数据,一个是发送的数据,一个是客户端的ip端口号
        udp_server.sendto(date.upper(),addr) #sendto() 发送数据,以及要送达的ip端口号
    except Exception as e:
        print(e)







