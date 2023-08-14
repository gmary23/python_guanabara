'''
Crie um programa que leia DOIS VALORES e mostre um MENU. Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5]sair do programa
    >>>>>> Qual é a sua opção? 
        ''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A Soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
    elif opcao == 4:
        print('Qual é a sua opção? ')
    elif opcao == 5:
        print('Finalizando programa.')
    else:
        ('Opção inválida, tente novamente...')
print('FIM')