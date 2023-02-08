import socket
import threading
import queue

messages=queue.Queue()
clients=[]
res=[['1','vvff'],['2','ffvfv'],['3','fff']]
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("localhost",3333))


def receive():
    while True:
        try:

            message, addr=server.recvfrom(1024)
            messages.put((message, addr))
        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            message, addr=messages.get()
            msg=message.decode()
            #print(message.decode())
            print(msg)
            if not message.decode().startswith("SIGNUP_TAG:"):

                msRes=trata(msg)
                print(msRes)
                
                server.sendto(f" {msRes}".encode(), client)
            if addr not in clients:
                clients.append(addr)
                for client in clients:
                    try:
                        if message.decode().startswith("SIGNUP_TAG:"):
                            #name=message.decode()[message.decode().index(":")+1:]
                            server.sendto(f"<N_DA_QUESTAO ; N_DE_ALTERNATIVAS ; RESPOSTAS>".encode(), client)
                        else:
                            server.sendto(message,client)
                    except:
                        clients.remove(client)


def trata( v):

    c=str(v)
    print(c)
    b=c.split(';')
    print(b)

    for x,d in res:
        print("questão "+x)
        if(x==b[0]):
            print(x+"e"+b[0])
            cont=0
            erros=0
            acertos=0
            for n in b[2]:
                num=int(b[0])-1
                print(n)
                if res[num][1][cont]==n:
                    print("acerto")
                    acertos+=1
                else:
                    print("errou")
                    erros+=1
                cont+=1
            
            msgCal="Questao "+x+' ; N_Acertos:'+str(acertos)+' ; N_Erros:'+str(erros)
            return msgCal

        
    return "essa questão nao existe"
      


t1=threading.Thread(target=receive)
t2=threading.Thread(target=broadcast)

t1.start()
t2.start()