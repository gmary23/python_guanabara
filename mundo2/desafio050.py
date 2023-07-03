'''
Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que
foram PARES. Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite o {}º número: '.format(n)))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A quantidade de números PARES são {cont} e a soma deles são {soma}')


