#Crie um programa que leia um número inteiro e mostre na tela se é par ou impar

n = int(input('Digite um numero e te digo se é impar ou par: '))

resto = n % 2

if resto == 0:
    print(f'Relaxa meu mano, {n} é par')
else:
    print(f'Meu mano, {n} é ímpar, demorou?')