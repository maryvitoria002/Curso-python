#Faça um programa que leia três números e mostre qual o maior e qual o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))
if n1 > n2 and n1 > n3:
    print (f'O maior número é {n1}')
elif n2> n1 and n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')

if n1 < n2 and n1 < n3:
    print (f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
else:
    print(f'E o menor número é {n3}')

