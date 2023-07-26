'''
Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um NÚMERO ENTRE 
O e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)
print('Estou pensando em um número, tente adivinhar.')
acertou =  False
palpite = 0
while not acertou:
    jogador = int(input('Digite um palpite: '))
    palpite += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos...Tente outro número.')
        elif jogador < computador:
            print('Mais...tente outro número.')
print('Acertou em {} tentativas. Parabéns!'.format(palpite))