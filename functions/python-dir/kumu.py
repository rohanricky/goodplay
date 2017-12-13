import sys
import socket
#Implement WebSockets for faster communication
# use gRPCs if the files get complex and microservices are a must

#Not working because firebase billing amount is not configured.
class Socket:
    def __init__(self,message_length,sock=None):
        if sock is None:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        else:
            self.sock=sock
        self.message_length=message_length

    def connect(self):
        self.sock.connect(('your-computer-ip-address',port no.))

    def sendtoserver(self,msg):
        total_sent=0
        self.sock.settimeout(3.0)
        print("Task Accomplished")
        while total_sent < self.message_length:
            sent=self.sock.send(msg[total_sent:])
            if sent==0:
                break
            total_sent+=sent
        self.sock.close()

if __name__ == '__main__':
    data = sys.argv[1]
    x=Socket(2048)
    x.connect()
    x.sendtoserver(data.lower())
