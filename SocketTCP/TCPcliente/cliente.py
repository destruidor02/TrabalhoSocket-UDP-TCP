import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost',4444))


namefile=str(input('Arquivo:'))

client.send(namefile.encode())

with open(namefile,'wb')as file:

    while 1:

        data = client.recv(1000000)
        if not data:
            break
        file.write(data)


print(f"{namefile} recebido!\n")