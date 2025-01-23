#O comando 'import' vai importar todas as funcioncionalidades do módulo (todos os recursos de uma biblioteca)

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

#sqrt = raiz quadrada
#floor = arredondar pra baixo
#ceil = arredondar pra cima
#trunc = truncar o numero sem arredondar, eliminar oq ta na frente da virgula
#pow = potência
#factorial = calcular fatorial

print(f'A raiz de {num} é igual a {raiz:.2f}')


#Enquanto o comando o comando 'from doce import pudim' (o doce e o pudim é um exemplo de biblioteca e funcionalidade respectivamente) é mais específico

from math import floor

print(f'A raiz de {num} com o floor é igual a {floor(raiz)}')
