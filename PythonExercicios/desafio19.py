#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

a1 = input('Digite o primeiro aluno: ')

a2 = input('O segundo: ')

a3 = input('O terceiro: ')

a4 = input('E o quarto: ')

e = random.choice([a1, a2, a3, a4])

print(f'O aluno que vai apagar o quadro vai ser {e}')