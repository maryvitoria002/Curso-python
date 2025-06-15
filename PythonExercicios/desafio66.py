#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
#entrada = 4, 6, 5, 999
#saida = a soma dos 3 valores foi 12
i = soma = 0
while True:
    n = int(input("Digite um inteiro (e 999 para parar): "))
    if n == 999:
        print('\nVocê finalizou a execução.')
        break
    i +=1
    soma += n
    
print(f"\nVocê digitou {i} números, e a soma deles foi {soma}!")