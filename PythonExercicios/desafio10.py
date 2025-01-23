#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = R$3.27

d = int(input('Quantos dinheiros você tem? '))

us = d / 3.27

print('R${} equivale a US${:.2f}.'.format(d, us))


