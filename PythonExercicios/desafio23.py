#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados (indicando desena, CENTENA etc)

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analizando o numero {num} podemos ver que ')

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar {m}')