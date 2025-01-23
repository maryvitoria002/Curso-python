#  Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

num = int(input('Digite o ângulo: '))

from math import sin, cos, tan, radians

seno = sin(radians(num))
cosseno = cos(radians(num))
tan = tan(radians(num))

print(f'O seno é {seno:.2f}\n O cosseno é {cosseno:.2f}\n A tangente é {tan:.2f}')