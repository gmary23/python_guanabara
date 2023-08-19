'''
Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar 
quando o usuário digirar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS  foram
digitados e qual foi a SOMA entre eles (desconsiderando o flag).
'''

n = 0
cont = 0
soma = 0
n = int(input('Digite um número [999 paraa parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 paraa parar]: '))
   
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont, soma))