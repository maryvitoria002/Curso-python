# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250.00, calcule um aumento de 10%. Para inferiores ou iguais o aumento é de 15%.

din = float(input('Qual seu salário atual? '))

if din > 1250:
    print(f'Cê vai ganhar um aumento de 10%, vai ficar com R${din + (din * 0.10)}')
else:
    print(f'Ganhou um aumento de 15%, vai ficar com R${din + (din * 0.15)}')