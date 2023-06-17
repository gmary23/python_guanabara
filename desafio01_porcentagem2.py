"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
"""

salario = float(input('Qual o valor do salário? '))
aumento = salario * 15 / 100
total = salario + aumento

print('O salário é {:.2f} com o aumento de 15% fica {:.2f}'. format(salario,total))
