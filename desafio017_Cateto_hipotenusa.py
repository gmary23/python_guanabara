"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot #importa da biblioteca matemática a função específica hypot que calcula hipotenusa
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))