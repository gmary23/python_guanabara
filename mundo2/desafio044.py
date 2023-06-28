"""
Elabore um programa que calcule o valor a ser pago por produto, considere o seu PREÇO NORMAL e
CONDIÇÃO DE PAGAMENTO:
1- à vista DINHEIRO/CHEQUE:
10% de desconto 
2- à vista CARTÃO: 5% de desconto
3- em até 2x NO CARTÃO: preço normal
4- 3x OU MAIS no cartão: 20% de juros
"""
compras = int(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista DINHEIRO/CHEQUE
[2] à vista CARTÃO
[3] 2x NO CARTÃO
[4] 3x OU MAIS no cartão 
      ''')
opcao = int(input('Qual é a opção? '))

opcao1 = compras -(compras *10)/100 
opcao2 = compras -(compras *5)/100 
opcao4 = compras +(compras *20)/100 
opcao4_1 = (compras *20)/100 

if opcao == 1:
    print('Sua compra de R$ {} vai custar R$ {} no final.'. format(compras, opcao1))
elif opcao == 2:
    print('Sua compra de R$ {} vai custar R$ {} no final.'. format(compras, opcao2))
elif opcao == 3:
    total = compras / 2
    print('Sua compra de R$ {} parcelado em 2x de {} e o preço final será {}.'. format(compras, total, compras))
elif opcao == 4 :
    parcelas = int(input('Quantas parcelas? '))
    total_juros = opcao4 / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'. format (parcelas, total_juros))
    print('Sua compra de R${} e vai custar R$ {} no final'. format (compras, opcao4))
else: 
    print('opcão inválida')
