import socket, threading
from string import punctuation

host = "IP_HERE"
port = PORT_HERE

username = input("enter username: ")

while any(char in punctuation for char in username) or len(username) > 10 or len(username) < 2 or " " in username or "THISISAUSERNAME" in username:
    print("\ninvalid username\n")
    username = input("enter username: ")

username += " THISISAUSERNAME"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send(username.encode())

def send():
    while True:
        message = input("")
        if len(message) != 0 and len(message) < 450:
            client.send(message.encode())

def listen():
    while True:
        try:
            print(client.recv(1024).decode())
        except:
            print("\nerror!!!!!!!!!!!!!!!\n")
            client.shutdown(socket.SHUT_RDWR)
            exit()

if __name__ == "__main__":
    threading.Thread(target=listen).start()
    threading.Thread(target=send).start()
