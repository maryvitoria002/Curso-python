# Cria um programa que simule o Funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) a o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considera que o caixa possui cédulas de R$50. R$20. R$10 R$1.

# banco mary
# qual valor voce quer sacar? 1234
# total de 24 cedulas de 50
# total 1 cedula de 20
# total de 1 cedula de 10
# total de 4 cedulas de 1
# ===================================
# volte sempre, tenha um bom dia

print('='*30)
print("        MARY'S BANCO        ")
print('='*30)
i = 1
cont50 = cont20 = cont10 = cont1= 0
valor = float(input("Qual valor você quer sacar? R$"))

while True:
    
    while 50 * i < valor:
        cont50 += 1
        i += 1

    i = 1

    if cont50 != 0:
        print(f"Total de {cont50} cédulas de R$50")
    
    valor = valor - cont50*50

    while 20 * i <= (valor):
        cont20 += 1
        i += 1
    
    i = 1

    if cont20 != 0:
        print(f"Total de {cont20} cédulas de R$20")
    valor = valor - cont20*20

    while 10 * i <= (valor):
        cont10 += 1
        i += 1
    
    i = 1

    if cont10 != 0:
        print(f"Total de {cont10} cédulas de R$10")
    valor = valor - cont10*10

    while 1 * i <= (valor):
        cont1 += 1
        i += 1

    if cont1 != 0:
        print(f"Total de {cont1} cédulas de R$1")

    
    print('\nVolte sempre ao nosso banco!')
    break





