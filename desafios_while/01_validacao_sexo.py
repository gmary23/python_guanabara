sexo = str(input('Digite o sexo [MF]: ')).strip().upper()[0]

while sexo not in 'MF':
   sexo = str(input('Digite a opção [MF]: ')).strip().upper()[0]
print('O sexo digitado foi {}'.format(sexo))