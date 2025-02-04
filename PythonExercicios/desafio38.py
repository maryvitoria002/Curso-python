#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segunto valor é maior ou nao existe valor maior, os dois sao iguais

n1 = int(input('Digite um número: '))
n2 = int(input('outro: '))

if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo é maior')
else:
    print('Os dois são iguais')