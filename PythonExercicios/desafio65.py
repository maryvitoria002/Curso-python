# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média de todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = maior = menor = i = 0
while True:
    num = int(input("Digite um número inteiro: "))
    soma += num
    if i == 0:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    i +=1
    desejo = input("Deseja continuar digitando valores? [S/N] ").upper()
    
    if desejo == 'N':
        break

media = soma/i
print(f'Você digitou {i} números. O maior número foi {maior}, o menor foi {menor} e a média foi {media}')