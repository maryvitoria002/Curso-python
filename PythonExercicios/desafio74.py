# Cria um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

# Depois disso mostre a listagem de números gerados a também Indique o manor co maior valor que estão na tupla.

import random

tupla = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))


print(f"Os números sorteados foram ", end=' ')
print(*tupla, end='')
print ("O máximo é")
print(max(tupla))
print ("O mínimo é")
print (min(tupla))