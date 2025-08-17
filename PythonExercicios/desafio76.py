# Cria um programa que tenha uma tupla única com nomes da produtos e seus respectivos preços. na sequência.

# No final, mostra uma listagem de prafos. organizando os dados am forma tabular.

tupla = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno',16.90,
         'Estojo',25,
         'Pasta',14.2,
         'Compasso',9.99,
         'Mochila',120.32,
         'Caneta',22.30)

print('-' * 40)
print(f'{"LISTA DE PREÇO":^40}')
print('-' * 40)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R${tupla[i]:>7.2f}')
