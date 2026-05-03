import socket

#Запуск серввера -> 24

ip_address='127.0.0.1'
port=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((ip_address, port))
    server_socket.listen()
    print(f'waiting for connection on {ip_address}:{port}')

    client_socket,client_address = server_socket.accept()

    with client_socket:
        print(f'client connected {ip_address}:{port}')

        data=client_socket.recv(1024)
        print(f'received {data}')

        response= data.upper()
        client_socket.sendall(response)
        print(f'sent {response}')
