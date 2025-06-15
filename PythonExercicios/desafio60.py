# Faça um programa que leia um numero qualquer e mostre o seu fatorial
# ex: 5! = 5*4*3*2*1= 120

# import math 

# n = int(input('Digite um número: '))


# print(math.factorial(n))

n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f)