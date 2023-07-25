'''
Faça um programa que leia o SEXO de uma pessoa, mas so aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Você não digitou uma opção válida. Digite seu sexo: ').strip().upper()[0]
print('O sexo é {} '.format(sexo))



