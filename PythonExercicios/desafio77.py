# Cria um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você dava mostrar para cada palavra, quais são as suas vogais.

tupla = ('Tom', 'Mary', 'Bruno', 'Maete')

for i in tupla:
    print(f"\nA palavra {i} possui ", end='')
    for letra in i:
        if letra.upper() in 'AEIOU':
            print(f"{letra}", end=' ')
    