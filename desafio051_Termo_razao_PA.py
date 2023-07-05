'''
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10) * razao
print(f'O decido é {decimo}')
for n in range(primeiro, decimo + razao, razao):
    print('{}'.format(n), end=' -> ')
print('ACABOU')