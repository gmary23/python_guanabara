"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
"""
valor = int(input('Qual valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Quantos anos quer pagar? '))

prestacao = valor/ (anos * 12)
minimo = (salario * 30)/ 100
print(minimo)
print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {}'.format(valor, anos, prestacao))

if prestacao <= minimo:
    print('O emprestimo será autorizado!')
else:
    print('O emprestimo será negado, pois a prestação mensal excedeu o valor do salário.')

   