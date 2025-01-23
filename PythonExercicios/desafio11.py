#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados

larg = int(input('Qual a largura ae? '))

alt = int(input('E a altura? '))

area= larg * alt

litro = area / 2

print('Sua área é de {} metros e você vai precisar de {} litros de tinta para pintá-la'.format(area, litro))