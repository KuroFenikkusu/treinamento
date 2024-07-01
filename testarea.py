# import do módulo random
from random import random

# Dicionario
moeda = {0: 'cara', 1: 'coroa'}

print('cara ou coroa?')
resposta = input('')

while resposta not in moeda.values():
    print("Por favor, digite apenas 'cara' ou 'coroa'")
    print('cara ou coroa?')
    resposta = input('')

flip = round(random())
res = moeda[flip]
print(f'A moeda deu: {res}')

if resposta == res:
    print('Ganho plim plim plom')
else:
    print('Perdeu troxa')
