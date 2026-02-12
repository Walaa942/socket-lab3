import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        message = client_socket.recv(1024).decode()
        print(f"Received from client: {message}")

        client_socket.send(f"Echo: {message}".encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
