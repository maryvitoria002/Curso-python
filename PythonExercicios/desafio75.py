# Desenvolva um programa qua leia quatro valores palo taciado a guarda-os em uma tupla. No final. mostre:

# A) Quantas vezes aparacau o valor 9.

# B) Em que posição foi digitado o primairo valor 3.

# C) Quais foram os números pares.

valores = list(map(int, input('Digite os valores: ').split()))
tupla = tuple(valores)
    
noves = tupla.count(9)
tres = tupla.index(3)


print(f'Tem {noves} números 9')
print (f'O número 3 foi digitado pela primeira vez na posição {tres}')
print ('Os números pares são: ')
for numero in tupla:
    if numero % 2 == 0:
        pares = numero
        print(pares, end='')

