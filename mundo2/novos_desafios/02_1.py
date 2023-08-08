'''
Escreva um programa que solicite ao usuário que insira números inteiros positivos
repetidamente até que ele insira um número negativo. O programa deve então calcular
e exibir a soma de todos os números positivos inseridos pelo usuário.
'''

soma = 0
num = int(input('Insira um número inteiro e positivo: '))

while num >= 0:
    soma += num
    num = int(input('Insira um número inteiro e positivo: '))
print('A soma entre os número é {}'.format(soma))