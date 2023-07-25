'''
Faça um programa que leia o peso de CINCO PESSOAS. No final, mostre qual foi o 
MAIOR e o MENOR peso lidos.
'''
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}a pessoa: '.format(p)))
    if p == 1: # aqui só entra qdo for a primeira pessoa
        maior = peso # maior recebe o peso
        menor = peso # menor recebe o peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} e o menor peso é {} '.format(maior, menor))
