"""
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
"""
c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5) +32 # equação de conversão de celsius para farenaite

print('A temperatura de {:.0f} ºC corresponde a {:.0f} ºF!'.format(c, f))
