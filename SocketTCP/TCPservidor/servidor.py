import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',4444))

print('Aguardando')

server.listen(1)

connection, address = server.accept()

namefile=connection.recv(1024).decode()

with open(namefile,'rb')as file:
    for data in file.readlines():
        connection.send(data)
    print('Arquivo enviado!!\n\nObrigado por usar o servidor DONIDONI')
    print('CONEXÃO FECHADA')

server.close()
