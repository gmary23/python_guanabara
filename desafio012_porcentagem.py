"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
"""
preco = float(input('Qual valor do produto? '))
desconto = (preco * 5) / 100
total = preco - desconto
print('O produto era {preco}, o desconto de 5% é {}, com desconto fica {}'.format(desconto, total))