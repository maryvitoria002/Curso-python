#Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range (0, 5):
    peso = float(input(f"Qual o {i+1}º peso? "))

    if i == 0:
        maior = peso
        menor = peso
    if (peso > maior):
        maior = peso
    elif peso < menor:
        menor = peso

print (f"O maior peso foi {maior}kg e o menor foi {menor}kg")