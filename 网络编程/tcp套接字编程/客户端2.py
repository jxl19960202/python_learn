from socket import *

client = socket(AF_INET,SOCK_STREAM)  #创建一个客户端
client.connect(('192.168.43.59',8008)) #连接服务端  注意:传入的参数必须是tuple
print('---------')
while True:
    date = input('请输入要发送的消息:')
    client.send(date.encode('utf-8'))  #收发消息只能是字节的形式,所以这里要编码
    res = client.recv(1024)   #字节
    print(res.decode('utf-8'))
client.close()