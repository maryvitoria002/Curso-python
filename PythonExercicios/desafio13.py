#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = int(input('Qual seu salário, divo? '))

aumento = (s * 0.15) + s

print('Com seu aumento você vai passar a receber R${}'.format(aumento))