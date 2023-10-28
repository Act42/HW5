import socket
import struct

def receive_message(sock):
    packed_len = sock.recv(4)
    message_len = struct.unpack("!I", packed_len)[0]
    message = sock.recv(message_len)
    return message.decode()

host = '0.0.0.0'
port = 12345

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(16)
        print("Server started, listening for connections...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                for i in range(100):
                    message = receive_message(client_socket)
                    print(f"Received message: {message}")
except Exception as ex:
    print(ex)
