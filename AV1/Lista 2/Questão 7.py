import random

def numero():
        num = random.randint(0,100)
        return num


numero_aleatorio = numero()

while True:

    numero_jogador = int(input('Digite um numero: '))


    if numero_jogador == numero_aleatorio:
        print('CORRETO!!')
        break
    elif numero_jogador < numero_aleatorio:
        print('o numero correto é maior\n')
    elif numero_jogador > numero_aleatorio:
        print('o numero correto é menor\n')