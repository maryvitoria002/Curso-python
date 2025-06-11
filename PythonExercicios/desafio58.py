# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar ate ele acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num = random.randint(0,10)
palp = 0

while True:

    ten = int(input('Tente acertar o número que o computador escolheu de 0 a 10: '))

    if ten == num:
        print(f'Parabéns, acertou!! o número é {num}')
        break

    else:
        print(f'Vixe, errou')
    palp += 1

print (f'Tu conseguiu errar {palp} vezes')
