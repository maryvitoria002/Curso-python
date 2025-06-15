# Cria um programa que leia a idade a o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

# No final, mostre:

# A)quantas pessoas tem mais de 18 anos.

# B)Quantos homens Foram cadastrados.

# C) Quantas mulheres tem menos de 20 anos.

# cadastre uma pessoa
# idade: 33
# sexo m/f: M
# quer continuar [s/n]:25
# quer continuar [s/n]:s

# idade: 25
# sexo [m/f]: g
# sexo [m/f]: r
# sexo [m/f]: f
# quer continuar? n

# no final desse programa o total de pessoas com mais de 18 anos: 2
# ao todo tem 1 homem cadastrado
# e 0 mulheres menorres de 20
maisd = homem = mulher = 0
while True:
    print('-'*30)
    print('Cadastre uma pessoa')
    print('-'*30)

    idade = int(input('Idade: '))
    if idade >= 18:
        maisd += 1
    sexo = input("Sexo: [M/F] ").upper()
    print('-'*30)
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <20:
        mulher += 1
    

    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == 'S':
        continue
    elif continuar =='N':
        break
    else: 
        print("Valor inválido")
        break

print(f'Há {maisd} pessoas +18')
print(f'Há {homem} homens')
print(f'Há {mulher} mulheres -20')


