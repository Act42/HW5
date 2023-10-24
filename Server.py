import socket
def server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Очікування підключення...")
    conn, addr = server_socket.accept()
    print(f"З'єднано з {addr[0]}:{addr[1]}")

    for i in range(100):
        message_length_bytes = conn.recv(4)
        message_length = int.from_bytes(message_length_bytes, byteorder='big')
        message = conn.recv(message_length)
        print(f"Сервер отримав: {message.decode('utf-8')}")

    conn.close()

if __name__ == "__main__":
    server()
