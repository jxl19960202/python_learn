#解决方案:给要发送的数据做一个报头(其中内容包括要发送信息的长度),接收端先获取该固定长度的报头(从中获得真实数据的
#长度),在接收该长度的真实数据.(如果数据太大,可以设置一个判断循环接收)

from socket import *
import struct

ip_port=('192.168.43.59',8080)
tcp_serve = socket(AF_INET,SOCK_STREAM)
tcp_serve.bind(ip_port)
tcp_serve.listen(5)

while True:
    coon,addr = tcp_serve.accept()
    while True:
        try:
            date = coon.recv(1024)
            res = date*10
            length_res = len(res)
            length = struct.pack('i',length_res)
            coon.send(length)
            coon.send(res)
        except Exception as e:
            print('发生错误')
            break



















