'''
Desafio: Contagem regressiva. Escreva um programa que utilize um loop "while"
para fazer uma contagem regressiva a partir de um número inserido pelo usuário. 
O programa deve pedir ao usuário para inserir um número inteiro positivo e, 
em seguida, imprimir uma contagem regressiva a partir desse número até 1.
'''

numero = int(input('Insira um número positivo inteiro: '))

if numero <= 0:
      print('Por favor insira um número primo inteiro.')

while numero >= 1:
      print('{} '.format(numero), end='')
      numero -= 1