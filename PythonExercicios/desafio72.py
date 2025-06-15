# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zaro até vinte.
# Seu programa deverá ler um número palo teclado (entre 0 a 20) e mostrá-lo por extenso.

numeros = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número entre 0 a 20: "))
    if num >=0 and num <= 20:
        break
    print("Número inválido.")

print (f'Você digitou o número {numeros[num]}')
