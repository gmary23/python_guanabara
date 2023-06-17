"""
Crie um algoritmo que leia um número e mostre seu dobro, triplo, e raiz quadrada
"""
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2) # faz a raiz quadrada

print('O número é {}, seu dobro é {}, o triplo é {} e sua raiz quadrada é {}'. format(n, d, t, r))

print()
print('OUTRA FORMA DE FAZER A MESMA COISA')
print()
o = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(o, (o*2)))
print('O triplo de {} vale {}. \nA raiz quadrade de {} é igual a {}.'.format(o, (o*3), o, pow(o, (1/2))))