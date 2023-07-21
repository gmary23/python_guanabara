"""
Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""
from datetime import date #importa a função data
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa) ))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else: 
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Também tivemos {} pessoas menores de idade'.format(totmenor))