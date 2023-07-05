'''
Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.

EXPLICAÇÃO - O número primo é divisível por 1 e por ele mesmo
'''
tot= 0
numero = int(input('Digite um número: '))
for c in range(1, numero +1):
    
    if numero % c == 0:
        print('\033[33m', end=' ') #esse caractere diferente são código de cores
        tot += 1 # se o número foi divisível então acrescenta mais um número no total
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
    
if tot == 2:
    print()
    print(f'O número {numero} é PRIMO')
else:
    print()
    print(f'O número {numero} NÃO É PRIMO')



