import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 12345

    client_socket.connect((host, port))

    message = "Hello, Server!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Server responded: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
