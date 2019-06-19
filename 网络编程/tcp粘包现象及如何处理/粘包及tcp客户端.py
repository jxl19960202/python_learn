from socket import *
import struct

ip_port=('192.168.43.59',8080)
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    res = input('--->')
    if not res:continue
    tcp_client.send(res.encode('utf-8'))
    lengh_res = tcp_client.recv(4)
    lengh = struct.unpack('i',lengh_res)[0] #获得真实数据的长度
    l = b""
    n = 0
    while n<lengh:
        l += tcp_client.recv(1024)
        n = len(l)
    print(l.decode('utf-8'))














