"""
Crie um programa que faça o computador jogar JOKENPÔ com você.
"""
from random import randint  
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual a sua jogada? '))
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
    
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O Computador ganhou')

#elif computador == 1: # COMPUTADOR JOGOU PAPEL

#elif computador == 2: # COMPUTADOR JOGOU TESOURA

  
      


