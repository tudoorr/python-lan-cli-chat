import socket, threading

host = "IP_HERE"
port = PORT_HERE
client_user_info = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def send_message(message, username):
    for client in client_user_info.keys():
        client.send((username + ": " + message).encode())

def await_message(client):
    while True:
        from_client = client.recv(1024).decode()
        username = client_user_info[client].strip("THISISAUSERNAME")
        username = username.strip()
        if "THISISAUSERNAME" not in from_client:
            send_message(from_client, username)

def new_user():
    while True:
        duplicate = False
        client = server.accept()[0]
        username = client.recv(1024).decode()
        for key in client_user_info.keys():
            if client_user_info[key] == username:
                client.send("\nusername unavailable\n".encode())
                client.shutdown(socket.SHUT_RDWR)
                duplicate = True
                break
        if duplicate == True:
            continue
        client_user_info[client] = username
        client.send("\nmessage from SERVER: ok connection\n\n".encode())
        threading.Thread(target=await_message, args=(client,)).start()

print("server start")
new_user()
