#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento = a vista dinheiro/cheque: 10% de desconto, a vista no cartao: 5% de desconto, em ate 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.

valor = float(input('Qual o valor da parada? R$'))
print('Dinheiro a vista: digite 1, a vista no cartão: 2, em até 2x no cartão: 3 e  mais parcelas: 4')
pag = int(input('Qual vai ser o método de pagamento? '))

if pag == 1:
    valor = valor - (valor*0.1)
    print(f'Você escolheu a opção 1: Pagar a vista no dinheiro, por isso ganhou 10% de desconto, então o valor vai ficar R${valor}')
elif pag == 2:
    valor = valor - (valor*0.05)
    print(f'Você escolheu a opção 2: Pagar a vista no cartão, por isso ganhou 5% de desconto, então o valor vai ficar R${valor}')
elif pag == 3:
    print(f'Você escolheu a opção 3: Parcelar em até 2x no cartão, o valor vai ficar R${valor}')
elif pag == 4:
    valor = valor + (valor*0.2)
    print(f'Você escolheu a opção 4: Parcelar em +2x no cartão, por isso será cobrado 20% de juros, então o valor vai ficar R${valor}')
