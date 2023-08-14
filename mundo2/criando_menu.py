'''
Crie um programa que leia DOIS VALORES e mostre um MENU.Seu programa deverá realizar a operação solicitada
em cada caso.
'''
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
[1] somar
[2] miltiplicar
[3] maior
[4] novos números
[5] sair do programa      
''')
    opcao = str(input('Qual é a sua opção: '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e o {} é {}'.format(primeiro, segundo, soma))
    elif opcao == 2:
        multiplica = primeiro * segundo
        print('A multiplicação entre {} e o {} é {}'.format(primeiro, segundo, multiplica))
    elif opcao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('maior')
    elif opcao == 4:
        print('>>>>>> Qual é a sua opção? ')
    elif opcao == 5:
        print('finalizado')
    else:
        print('Opção inválida, tente outro número.')
    
print('FIM')