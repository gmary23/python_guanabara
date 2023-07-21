'''
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
- A MÉDIA DE IDADE do grupo.
- Qual é o nome do homem MAIS VELHO.
- Quantas mulheres têm MENOS DE 20 anos.
'''
somaidade = 0
mediaidade = 0
for p in range (1, 5):
    print('--------{}ª PESSOA ---------'.format(p))
    nome = str(input('Nome: ')).strip() #strip -> retira espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

mediaidade = somaidade / 4
print('A média de idade das pessoas é de {}'.format(mediaidade))
