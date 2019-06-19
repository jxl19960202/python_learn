from socket import *

udp_client = socket(AF_INET,SOCK_DGRAM)
ip_port =('192.168.43.59',8008)
buf_size = 1024

while True:
    msg = input('===>:')
    if not msg:continue    #判断发送消息是否为空,为空则重新发送
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    res,addr = udp_client.recvfrom(buf_size)
    print(res.decode('utf-8'))
udp_client.close()