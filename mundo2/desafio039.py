"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo 
com a sua idade , se ele AINDA VAI SE ALISTAR ao serviço militar, se é a HORA DE SE ALISTAR
ou se ja PASSOU DO TEMPO do alistamento. Seu programa também deverá mostrar o tempo que 
falta ou que passou do prazo.
"""
from datetime import date # importa o módulo datetime especificamente a date
nascimento = int(input('Ano de Nascimento: '))

ano_atual = date.today().year
idade = ano_atual - nascimento
falta = idade - 18
ano_alistamento = ano_atual - falta
print('Quem nasceu em {}, tem {} anos em {}'.format(nascimento, idade, ano_atual))

if idade < 18:
    print('Ainda falta {} anos para o alistamento. Seu alistamento será em {} '.format(falta, ano_alistamento))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos. O período do seu alistamento foi(é) {}' .format(idade,falta, ano_alistamento))
else: 
    print('se aliste imediatamente')

