'''
Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL
'''
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n # o c recebe n porque o fatorial de um número começa dele mesmo e vai até o 1
f = 1 # aqui é 1 pq é o fator nulo de multiplicação.
while c > 0: # aqui é maior do que zero pq ele vai até o número 1
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    
print('{}'.format(f)) # esse precisa está fora do calculo para executar