'''
Crie um programa que leia DOIS VALORES e mostre um MENU como mostra abaixo:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso.
'''
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é {}'. format(primeiro, segundo, soma))
    
    elif opcao == 2:
        produto = primeiro * segundo
        print(' {} * {} = {}'.format(primeiro, segundo, produto))
    
    elif opcao == 3:
        if primeiro > segundo:
            print('O número maior é {}'.format(primeiro))
        else:
            print('O número maior é {}'.format(segundo))

    elif opcao == 4:
        print('Informe os número novamente')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=_=' * 10)
print('Fim de programa! Volte sempre!')
