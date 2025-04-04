assentos = list(range(1,101)) # Lista com 100 assentos

def reservar_assento (lista):
    try:
        lista_reservados = [int(assento.strip()) for assento in lista.split(',')]
        
        for num in lista_reservados:
            if num in assentos:
                assentos.remove(num)
                print(f'Foi reservados os assento {num}')
            else: 
                print(f"Assento {num} não está disponível.")
    except ValueError:
        print(ValueError)
    


print('Seja bem vindo ao cinema')
while True:
    entrada = input('Digite o numero do assento(s) que você deseja reservar: ')
    
    reservar_assento(entrada)
    
    saida = input('Deseja reservar mais um assento? s = sim, n = nao (s/n)')
    if saida != 's':
        break


print("\nAssentos restantes:", assentos)
print("Obrigado pela sua reserva!")