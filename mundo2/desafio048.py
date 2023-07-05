'''
Faça um programa que calcule a SOMA entre todas os NÚMEROS ÍMPARES que são
MÚLTIPLOS DE TRÊS e que se encontram no intervalor de 1 até 500.
'''
soma = 0
cont = 0
for c in range(1, 501, 2): # conta até 500
    if c % 3 == 0:
        soma += c # para fazer soma tem de usar o conceito de acumulador
        cont += 1 # conta a quantidade de números foram somados
        #print(c, end=' ')
print('A soma de todos os números é {}'.format(soma))
print('A quantidade de números somados foi {}'.format(cont))

        
