#fAÇA UM PROGRAMA QUE LEIA UM Número inteiro e diga se ele é ou não um número primo.

print ("="*20)
print ("   É PRIMO OU NÃO?")
print ("="*20)

num = int(input("Digite um número: "))
tot = 0
for i in range (1, num+1):
    if num % i == 0:
        print ("\033[32m")
        tot += 1
    else:
        print ("\033[31m")
    print(i, end='')

    
print (f"""\033[m

O número {num} foi divisível {tot} vezes""")

if tot == 2:
    print ("É PRIMO")
else:
    print("NÃO É PRIMO")

