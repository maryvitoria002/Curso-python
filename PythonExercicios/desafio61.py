# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print ("="*40)
print ("      10 PRIMEIROS TERMOS DE UMA PA")
print ("="*40)

a1= int(input("Digite o 1º termo: "))
r= int(input("Digite a razão: "))

i= 1
while i < 11:
    n = a1 + (i - 1)* r
    print (n, end=' => ')
    i+=1
print ("E só")