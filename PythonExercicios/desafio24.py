#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'

cidade = str(input('Qual a cidade? ')).upper()

c = cidade.split()

print('SANTO' in c[0])
