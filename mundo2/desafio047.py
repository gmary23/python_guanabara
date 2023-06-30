'''
Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no inter-
valor entre 1 e 50.
'''
for n in range(1, 51):
    if n % 2 == 0: # se o número for divisível por 2
        print(n, end=' ') # será impresso apenas os número pares - O end=" " continua na linha e com espaço entre os números
print('Acabou')