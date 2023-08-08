'''
Escreva um programa que solicite ao usuário que insira números inteiros positivos
repetidamente até que ele insira um número negativo. O programa deve então calcular
e exibir a soma de todos os números positivos inseridos pelo usuário.
'''
numero = int(input('Digite um número: '))
cont = 0
while numero >=1:
    numero = int(input('Digite um número: '))
    if numero < 0:
        cont += numero
print('A soma dos números é {}'.format(cont))

  
