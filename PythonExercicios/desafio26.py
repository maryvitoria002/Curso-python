#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra 'A'. Em que posição ela aparece pela primeira vez e pela última.

frase = (str(input('Digite a frase: ')).upper()).strip()

print(f'A letra A aparece {frase.count('A')} vezes na frase')
print(f'A letra A aparece pela primeira vez na posição {frase.find('A') + 1}')
print(f'A letra A aparece pela última vez na posição {frase.rfind('A') + 1}')