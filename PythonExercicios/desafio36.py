#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. (elif) (pegar o valor da casa, dividir pelas parcela e todo mes ce vai ter que me pagar tanto, mas se o valor mensal exceder os trinta por cento ele nao pode finaciar)t

vc = float(input('Qual o valor da casa? '))
sc = float(input('Qual seu salário? '))
anos = float(input('Em quantos anos voce vai pagar? '))

prestacao = vc / (anos*12)

if prestacao > (sc * 0.3):
    print(f'A prestação ficou no valor de R${prestacao:.2f}, não foi aprovado')
else: 
    print(f'A prestação ficou no valor de R${prestacao:.2f}, foi aprovado')
