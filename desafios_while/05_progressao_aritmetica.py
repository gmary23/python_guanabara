'''
Leia o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura WHILE
'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro # o termo começa no número escolhido
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao # aqui vai somar o número com a razão
    cont += 1 # vai pegar o próximo número
print('FIM')