'''
Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL.
Ex. 
5! = 5x4x3x2x1 = 120
USANDO O FATORIAL DO MODO TRADICIONAL
'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n # o fatorial começa com ele mesmo - então o número que acabou de digitar é n
f = 1 # o fator nulo de multiplicação é 1 - quer dizer que todo número multiplicado por 1 é ele mesmo
print('Calculando {}!='.format(n), end='')
while c > 0: # pq o fatorial vai até 1
    print('{}'.format(c), end='') # o end é para não pular de linha
    print(' x ' if c > 1 else ' = ', end='') # é possível colocar if dentro de print
    f *= c
    c -= 1
print('{}'.format(f))

