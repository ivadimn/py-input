import socket
from select import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5001))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        print("Before .accept()")
        client_socket, addr = server_socket.accept()
        client_socket.send("Link OK!!\n".encode())
        print("Connection from", addr)

def send_message(client_socket):
    while True:
        print("Before .recv()")
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = "Hello client\n".encode()
            client_socket.send(response)
    client_socket.close()


def event_loop():
  pass


if __name__ == "__main__":
    pass
