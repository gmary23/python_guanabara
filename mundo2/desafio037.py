"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
1 para binário
2 para octagonal
3 para hexadecimal
"""

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das opção para realizar conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAGONAL
[ 3 ] converter para HEXADECIMAL
''')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'. format(numero, bin(numero)[2:])) # o python sozinho já faz a conversão usando (bin, oct e hex) - veja nos exemplos abaixo
elif opcao == 2:
    print('O número {} convertido para OCTAGONAL é {}'. format(numero, oct(numero)[2:])) # esse [2:] é o fatiamento, ou seja ele fatiou/cortou após a segunda casa...veja o exemplo sem fatiamento
    print('O número {} convertido para OCTAGONAL é {}'. format(numero, oct(numero))) # aqui sem fatiamento
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'. format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')
