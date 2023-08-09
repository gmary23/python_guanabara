'''
jogo de adivinhação
'''
from random import randint # comando importa número inteiro aleatório

computador = randint(0, 10)

print('Olá pensei em um número')
acertou = False
palpite = 0

while not acertou:
    jogador=int(input('Digite um número: '))
    if jogador == computador:
        palpite += 1
        acertou = True
    else:
        if jogador > computador:
            print('Escolha um número menor')
        elif jogador < computador:
            print('Tente um número maior.')
print('Você acertou!')


