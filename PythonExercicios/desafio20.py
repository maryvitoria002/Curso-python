#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

a1 = input('Digite o primeiro aluno: ')

a2 = input('O segundo: ')

a3 = input('O terceiro: ')

a4 = input('E o quarto: ')

import random

e = [a1, a2, a3, a4]

random.shuffle(e)

print(f'E a ordem de apresentação será {e}')