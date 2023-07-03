'''
Refaça o DESAFIO 09, mostrando  a TABUADA de um número que o usuário escolher,
só que agora utilizando um LAÇO FOR.
'''
num = int(input('Digite um número: '))
c = 0
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c ))
    print()
    #print(f'{num} x {c} = {num*c}')
    c += 1
    