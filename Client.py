import socket
import struct

def send_message(sock, message):
    message_len = len(message)
    packed_len = struct.pack("!I", message_len)
    sock.sendall(packed_len)
    sock.sendall(message.encode())

host = '127.0.0.1'
port = 12345

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        for i in range(100):
            message = f"message {i + 1}"
            send_message(client_socket, message)
            print(f"Message sent: {message}")
except Exception as ex:
    print(ex)
