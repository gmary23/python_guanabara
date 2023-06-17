a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace()) # verifica se só tem espaços
print('Só tem numeros? ', a.isnumeric()) # verifica se é só número
print('É alfabetico? ', a.isalpha()) # verifica se é só letras
print('Só é alfanuméricos? ', a.isalnum()) # verifica se tem letras e números
print('Está em maiúsculas? ', a.isupper()) # verifica se só tem letras maiúsculas
print('Está em minusculas? ', a.islower()) # verifica se só tem minustuculas
print('Está capitalizada? ', a.istitle()) # verifica se ñ está maiuscula nem minuscula / ou seja pode ter as duas, mas nunca apenas uma
