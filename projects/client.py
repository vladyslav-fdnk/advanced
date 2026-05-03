import socket


ip_address='127.0.0.1'
port=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((ip_address, port))
    client_socket.sendall(b'GET / HTTP/1.1\r\nHello Server!\r\n\r\n')
    data = client_socket.recv(1024)



    print(f'received {data.decode('utf-8')}')