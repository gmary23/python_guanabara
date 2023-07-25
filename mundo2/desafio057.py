'''
Faça um programa que leia o SEXO de uma pessoa, mas so aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo =str(input('Dados inválido, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


