#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo
#Qual o nome do homem mais velho
#quantas mulheres tem menos de 20 anos.
# 

somaidade= 0 
mediaidade= 0
maioridade = 0
cont = 0
for i in range (1, 5):
    print(f'-----{i}º  PESSOA: ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input("Sexo M/F: ")).strip()
    somaidade += idade
    if sexo == "M":
        if idade > maioridade:
            maioridade = idade
            homem = nome
    if sexo == "F":
        if idade < 20:
            cont +=1



mediaidade = somaidade/4
print(f'A média da idade é {mediaidade} anos')
print (f'O homem mais velho é {homem}')
print(f"{cont} mulheres são menores que 20 anos")
 