# Cliente/Servidor 01

# Importando os módulos
import socket
from threading import Thread

# Servidor
def servidor():
    ip_servidor = "10.0.0.106"
    porta_servidor = 32092   

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

    sock.bind((ip_servidor, porta_servidor)) 
     
    while True:
        pacote, endereco = sock.recvfrom(1024)
        if (pacote.decode('utf-8') == "QUIT"):
            sock.close()
            break
        print(f"[Cliente 2]: {pacote.decode('utf-8')}")

# Cliente
def cliente():
    ip_destino = "10.0.0.106"
    porta_destino = 32002

    while True:
        mensagem = str(input(">> "))
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.sendto(mensagem.encode('UTF-8'), (ip_destino, porta_destino))

if __name__ == '__main__':
    Thread(target = servidor).start()
    Thread(target = cliente).start()
