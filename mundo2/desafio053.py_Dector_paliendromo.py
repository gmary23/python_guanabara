'''
PALÍNDROMO - SÃO PALAVRAS QUANDO ESCRITAS DE TRÁS PARA FRENTE TEM O MESMO SENTIDO
Ex. APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANATARAM A DATA DA MARATONA

Crie um programa que leia uma FRASE qualquer e diga se ele é um PALÍNDROMO, desconsiderando os espaços.

frase = str(input('Digite a frase: ')).strip().upper() #.strip -> retira os espaços antes e depois / .upper -> transforma em MAIÚSCULA
palavras = frase.split() # na variável palavra colocou a frase fatiada é o que faz a função .split()
junto =  ''.join(palavras) #juntou tudas as partes
inverso = ''
for letra in range(len(junto)-1, -1, -1): 
    inverso += junto[letra]
if inverso == junto:
    print(f'A palavra {frase} é um palídromo')
else:
    print(f'A palavra {frase} não é um palídromo')
    '''
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print(f'A palavra {frase} é palindromo')
else:
    print(f'A palavra {frase} NÃO é palindromo')


#print(junto)

