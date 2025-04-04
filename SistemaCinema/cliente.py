import socket

# CONFIG SERVER

HOST = '127.0.0.1'
PORT = 65432

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST,PORT))

print('Seja bem vindo ao cinema')

while True:
    entrada = input('Digite o numero do assento(s) que você deseja reservar: ')
    cliente.sendall(entrada.encode())
    
    resposta = cliente.recv(1024).decode()
    print(resposta)
    
    saida = input('Deseja reservar mais um assento? s = sim, n = nao (s/n)')
    if saida != 's':
        break

cliente.close()
print("Conexão encerrada.")