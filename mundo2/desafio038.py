'''
Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na 
tela uma mensagem:
- O PRIMEIRO VALOR é maior
- O SEGUNDO VALOR é maior
- NÃO EXISTE valor maior, os dois são iguais
'''
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro > segundo:
    print('O primeiro numero é maior.')
elif segundo > primeiro:
    print('O segundo número é maior.')
else:
    print('Os números são iguais.')
