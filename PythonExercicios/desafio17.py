#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

ca = float(input('Digite o valor do cateto adjacente: '))

co = float(input('Digite o valor do cateto oposto: '))

from math import sqrt, hypot

hip = sqrt(ca**2 + co**2)

print(f'A hipotenusa tem o valor de {hip:.2f}')

hip2 = hypot(co,ca)

print(f'A hipotenusa (usando o módulo) tem o valor de {hip2:.2f}')

