#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridades e quantas já são maiores. Considere 21 anos a maioridade.
maior = 0
menor = 0
for i in range(0, 7):
    idade = int(input(f"Digite a {i+1}º idade: "))
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print (f"Tem {maior} pessoas de maior e {menor} pessoas de menor")