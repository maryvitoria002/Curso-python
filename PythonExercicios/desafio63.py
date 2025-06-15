# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci. ex: 0 - 1 - 1 - 2 - 3 - 4 - 8

n = int(input("Digite quantos termos deseja: "))

t1 = 0
t2 = 1
i = 3
print(f"{t1} -> {t2}", end='')
while i <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    i+=1
    
