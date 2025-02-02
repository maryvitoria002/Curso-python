#Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça pra o usuário tentar descobrir qual foi o número escolhido pelo computador (o pr)

ten = int(input('Tente acertar o número que o computador escolheu de 0 a 5: '))

import random

num = random.randint(0,5)

if ten == num:
    print(f'Parabéns, acertou!! o número é {num}')
else:
    print(f'Vixe, errou, era {num}')
