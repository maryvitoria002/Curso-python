#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = int(input('Qual o preço do produto? '))

d = preco * 0.05
vd = preco - d

print('O produto, com os 5% de desconto fica R${}'.format(vd))