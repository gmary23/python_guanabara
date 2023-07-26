'''
Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL.
Ex. 
5! = 5x4x3x2x1 = 120
O Python tem um módulo que importa e já faz o fatorial rapidinho
'''
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))