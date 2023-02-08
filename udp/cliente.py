import socket
import threading
import random

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000,9000)))

name = input("Nome: ")

def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print("\n"+message.decode())
        except:
            pass

t=threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(),("localhost",3333))
while True:
    message=input("")
    if message=="!q":
        exit()
    else:
        client.sendto(f"{message}".encode(),("localhost",3333))
