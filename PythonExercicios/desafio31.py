#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200Km e R$0.45 para viagens mais longas

d = int(input('Qual a distancia da sua viagem em km? '))

if d <= 200:
    print(f'Sua viagem vai custar R${d*0.50}')
else:
    print(f'Sua viagem vai custar R${d * 0.45}')