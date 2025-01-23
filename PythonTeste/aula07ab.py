n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))

#Coloquei o resultado da divisão com 3 casas decimais flutuantes

print('Divisão inteira {} e a portência é {}'.format(di, e))

#se eu não quiser que haja uma quebra de linha eu coloco ,end=''

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e a portência é {}'.format(di, e))

#se eu quiser que haja uma quebra de linha eu coloco \n

print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e a portência é {}'.format(di, e))