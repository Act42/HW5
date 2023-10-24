import socket
def client():
    host = "127.0.0.1"
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    for i in range(100):
        message = f"Повідомлення номер {i + 1}".encode('utf-8')
        message_length = len(message)
        client_socket.send(message_length.to_bytes(4, byteorder='big'))
        client_socket.send(message)

    client_socket.close()

if __name__ == "__main__":
    client()
