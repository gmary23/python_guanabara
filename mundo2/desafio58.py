'''
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um NÚMERO ENTRE 
O e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)
palpite = 0
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False # começa com false pq não acertou ainda
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
       acertou = True
    else:
        if jogador > computador:
            print('Menos...Tente outro número')
        elif jogador < computador:
            print('Mais...Tente outro número')

print('Acertou em {} tentativas'.format(palpite))