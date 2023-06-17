"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
U$ = 4,81
Euro = 5,28
"""
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.81
euro = real /5.28
print('Você tem {:.2f} dolares'.format(dolar))
print('Você tem {:.2f} dolares'.format(euro))