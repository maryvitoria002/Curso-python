#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print ("="*40)
print ("      10 PRIMEIROS TERMOS DE UMA PA")
print ("="*40)

a1= int(input("Digite o 1º termo: "))
r= int(input("Digite a razão: "))

for i in range (1, 11):
    n = a1 + (i - 1)* r
    print (n, end=' => ')
print ("E só")