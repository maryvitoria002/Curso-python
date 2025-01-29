#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ex: Ana Maria de Souza. Primeiro: Ana Último: Souza.

nome = str(input('Digite seu nome completo: ')).strip()

n1 = nome.split()

print(f'O primeiro nome é: {n1[0]} e o último é {n1}')