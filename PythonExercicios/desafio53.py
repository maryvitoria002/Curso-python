#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = str(input("Digite uma frase ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =  ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print ("É palíndromo")
else:
    print ("Não é palíndromo")