#
from socket import *

ip_port=('192.168.43.59',8008)
client = socket(AF_INET,SOCK_STREAM)  #创建一个客户端
client.connect(ip_port) #连接服务端 ,建立双向链接 注意:传入的参数必须是tuple
print('---------')
while True:
    date = input('请输入要发送的消息:')
    if not date:continue  #判断如果输入为空,请重新输入
    client.send(date.encode('utf-8'))  #收发消息只能是字节的形式,所以这里要编码
    res = client.recv(1024)   #字节
    print(res.decode('utf-8'))  #收到的是字节,需要解码
client.close()
















