#Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado -  equilátero: todos os lados iguais, isósceles: dois lados iguais, escaleno: todos os lados diferentes.

l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
   if l1 == l2  == l3:
    print('Da pra formar um triângulo equilátero')
   elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Dá pa fazer um triângulo isósceles')
   else:
     print('Dá pa fazer um triângulo escaleno')

else:
    print('Da pa fazer nao irmao')


