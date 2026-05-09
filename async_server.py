import selectors
import socket

sel= selectors.DefaultSelector()

def read_client(client_socket):
    data = client_socket.recv(1024)
    if not data:
        sel.unregister(client_socket)
        client_socket.close()
        print(f'client closed {client_socket}')
        return

    client_socket.send(f"{b'echo'} {data})")

def accept_client(server_socket):
    client_socket, client_address = server_socket.accept()
    client_socket.setblocking(False)
    print(f'accepted connection from {client_address}')
    sel.register(client_socket,selectors.EVENT_READ,read_client)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen()
server.setblocking(False)
sel.register(server,selectors.EVENT_READ,accept_client)

print('Event loop running on localhost:8080')

while True:
    events = sel.select(timeout=1)
    for event_key, event_mask in events:
        callback = event_key.data
        callback(event_key.fileobj)