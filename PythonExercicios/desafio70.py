# Crie um programa que leia o nome co preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# A) Qual é o total gasto na compra.

# B) Quantos produtos custam mais de R$1000.

# C) Qual é o nome do produto mais barato.

# nome do produto: mouse
# preço: 50
# quer continuar? [s/n]: s
# nome do produto: caneta
# preço: 3
# quer continuar? [s/n]: s
# nome do produto: notebook
# preço: 2550
# quer continuar? [s/n]: s
# nome do produto: impressora
# preço: 800
# quer continuar? [s/n]: s
# nome do produto: monitor
# preço: 1250
# quer continuar? [s/n]: n
# fim do programa
# o total da compra foi 4653,00
# temos 2 produtos custando mais de 1000,00
# o produto mais barato foi caneta que custa 3
soma = maismil = i = 0
nomemenor = ''
while True:
    print('-'*30)
    print('     Lojona da Marocas')
    print('-'*40)
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    if i == 0:
        menor = preco
    if preco < menor:
        menor = preco
        nomemenor = nome
    if preco > 1000:
        maismil += 1
    soma += preco
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        print('------- FIM DO PROGRAMA -------')
        break
    i += 1
    
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {nomemenor} que custa R${menor}')
