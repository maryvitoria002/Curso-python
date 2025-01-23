#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = int(input('Digite seu valor em metros: '))

cm = m*100

mm = m*1000

print('{} metros equivale a\n {} centímetros\n {} milímetros'.format(m, cm, mm))