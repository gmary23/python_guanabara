'''
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:
- A MÉDIA DE IDADE do grupo.
- Qual é o nome do homem MAIS VELHO.
- Quantas mulheres têm MENOS DE 20 anos.
'''
somaidade = 0
mediaidade = 0
idade_homem_mais_velho = 0
nome_dumaisvelho = ''
totIdadeMulher = 0
for p in range (1, 5):
    print('--------{}ª PESSOA ---------'.format(p))
    nome = str(input('Nome: ')).strip() #strip -> retira espaços
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        idade_homem_mais_velho = idade
        nome_dumaisvelho = nome
    if sexo in "Mm" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_dumaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totIdadeMulher += 1

mediaidade = somaidade / 4
print('A média de idade das pessoas é de {}'.format(mediaidade))
print('O nome do mais velho é {} e sua idade é {}'.format(nome_dumaisvelho, idade_homem_mais_velho))
print('São {} mulheres com menos de 20 anos'.format(totIdadeMulher))


