#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

km = int(input('Quantos km tu percorreu? '))
d = int(input('Por quantos dias tu alugou o carro? '))

skm = km * 0.15
sd = d * 60

total = sd + skm

print(f'O total que tu tem que pagar é R${total}')
