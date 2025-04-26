#Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC (Para calcular o IMC, divida o seu peso (em quilos) pela sua altura (em metros) elevada ao quadrado, ou seja, altura x altura.) e mostre seu status de acordo a tabela = abaixo de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal, 25  até 30: sobrepeso, de 30 ate 40: obesidade, acima de 40: obesidade mórbida.

p = float(input('Qual seu peso? '))
a = float(input('E sua altura? qual é? '))

imc = p / (a*a)
if imc < 18.5:
    print(f'Você está abaixo do peso man, seu imc tá {imc:.2f}')
elif 18.5 < imc < 25:
      print(f'carai borracha, seu imc tá {imc:.2f}, no ponto')
elif 25 < imc < 30:
     print(f'carai borracha, seu imc tá {imc:.2f}, acima do peso, sobrepeso')
elif 30 < imc < 40:
     print(f'carai borracha, seu imc tá {imc:.2f}, CE TA OBESO')
else:
      print(f'{imc:.2f} de imc? SEU GORDO VC VAI MORRER')