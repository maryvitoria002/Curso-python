# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for

n = int(input('Digite um número: '))

for i in range (0, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")