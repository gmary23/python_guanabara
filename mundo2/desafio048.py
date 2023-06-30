'''
Faça um programa que calcule a SOMA entre todas os NÚMEROS ÍMPARES que são
MÚLTIPLOS DE TRÊS e que se encontram no intervalor de 1 até 500.
'''
soma = 0
for c in range(1, 500, 2): 
    if c % 3 == 0: # verifica se o número é divisível por 3
        soma = soma + c
print('A soma de todos os valores solicitados é {}'.format(soma))