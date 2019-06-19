import socketserver  #利用socketserver,实现tcp协议并发
#server类:处理链接的 request类:处理通讯的

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request,self.client_address) #request是链接,client_address是客户端的ip及端口
        while True:
            try:
                date = self.request.recv(1024)  #收消息
                self.request.sendall(date.upper())  #发消息
            except Exception as e:
                print('发生错误')
                break

ip_port = ('192.168.43.59',8008)
if __name__ == '__main__':               #这里实现链接循环,多并发
    s = socketserver.ThreadingTCPServer(ip_port,Myserver)
    s.serve_forever()








