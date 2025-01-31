n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

print(f'Sua média foi {m}')


if m >= 6.0:
    print('Qua, tá bom')
else:
    print('Média de merda')

print('Parabens até' if m >= 6 else 'Estude mais')
