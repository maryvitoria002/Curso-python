#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.0 para cada Km acima do limite

mk = int(input('Qual a velocidade do seu carro em KM? '))

if mk > 80:
    print (f'Então meu mano, tu foi multado por excesso de velocidade e a multa é de R${(mk - 80)*7}')
else:
    print('Tá tudo certo então meu mano, segue assim.')