import socket
import argparse

def server_tcp(target,port):

    server_bind = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_bind.bind((target,port))
    server_bind.listen()
    print(f'listening on {target} {port}')
    client_sock,addr = server_bind.accept()
    
    while client_sock:
        try:
            
            print(f'recived connection from {addr[0]} {addr[1]}')
            print(client_sock.recv(2048).decode())

        except KeyboardInterrupt:
            exit(0)

def client_sender(target,port):

    client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_sock.connect((target,port))

    while 1:
        try:

            resp = ""
            resp_len = 1

            while resp_len:

                data = client_sock.recv(4096)
                resp_len = len(data)
                resp += data

                if resp_len > 4096:
                    break

                print(resp.decode())
                
                buffer = input("").encode()
                buffer += "\n"

                client_sock.send(buffer)

        except:
            exit(0)




if __name__ == '__main__':
    client_sender('google.com',443)
    