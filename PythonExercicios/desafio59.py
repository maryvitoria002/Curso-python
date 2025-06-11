# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

# seu programa deverá realizar a operação solicitada em cada caso
import time
op = 0 
while op != 5:
    n1, n2 = map(int, input("Digite dois números: ").split())

    while op != 5:
        time.sleep (1)
        print ("""    -------------
    [1]somar
    [2]multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    ---------------""")
        op = int(input('>>>> Qual sua opção? '))
        if op == 1:
            print (f"{n1} + {n2} = {n1+n2}")
        elif op == 2:
            print (f"{n1} * {n2} = {n1*n2}")
        elif op == 3:
            if n1 > n2:
                print (f"Entre {n1} e {n2} o maior é {n1}")
            elif n1 == n2:
                print('Mesmo valor')
            else:
                print (f"Entre {n1} e {n2} o maior é {n2}")
        elif op == 4:
            break
