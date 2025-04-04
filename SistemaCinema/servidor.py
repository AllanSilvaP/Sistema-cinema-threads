import socket
import threading

assentos = list(range(1, 101))  # Lista com 100 assentos
lock = threading.Lock()

def reservar_assento(conexao, endereco):
    print(f"Novo cliente conectado: {endereco}")
    
    try:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break  # Cliente desconectou

            dados = dados.decode()
            try:
                lista_reservados = [int(assento.strip()) for assento in dados.split(',')]
            except ValueError:
                conexao.sendall("Entrada inválida! Digite apenas números separados por vírgula.\n".encode())
                continue

            with lock:
                mensagem = ""
                for num in lista_reservados:
                    if num in assentos:
                        assentos.remove(num)
                        mensagem += f'Assento {num} reservado com sucesso.\n'
                    else:
                        mensagem += f"Assento {num} não está disponível.\n"

                conexao.sendall(mensagem.encode())
    except (ConnectionResetError, ConnectionAbortedError):
        print(f"Cliente {endereco} desconectado inesperadamente.")
    except Exception as e:
        print(f"Erro com o cliente {endereco}: {e}")
    finally:
        conexao.close()
        print(f"Cliente {endereco} desconectado.")

# CONFIGURAÇÃO DO SERVIDOR

HOST = '127.0.0.1'
PORT = 65432

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen(5)

print("Servidor de reservas iniciado. Aguardando conexões...")

while True:
    try:
        conexao, endereco = servidor.accept()
        thread_cliente = threading.Thread(target=reservar_assento, args=(conexao, endereco))
        thread_cliente.start()
    except KeyboardInterrupt:
        print("\nServidor encerrado manualmente.")
        servidor.close()
        break
