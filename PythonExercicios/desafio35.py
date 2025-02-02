#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou nao formar um triângulo.

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Dá pa fazer um triangulo irmone')
else:
    print('Da pa fazer nao irmao')
