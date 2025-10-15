import socket
import argparse
import threading


def server_tcp(port):

    server_bind = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_bind.bind(('0.0.0.0',port))
    server_bind.listen(1)

    while 1:
        client_sock,addr = server_bind.accept()
        print(f'recived connection from {addr}')



if __name__ == '__main__':
    server_tcp(9000)