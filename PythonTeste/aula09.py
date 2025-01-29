# Fatiamento

# Fatiar uma string é separar ela em partes

frase = 'Curso em video Python'

print(frase)

# O colchete indica lista

print(frase[9])
# Ele vai pegar somente a letra na posição 9, contando os espaços e começando do 0

print(frase[9:13])
# Ele vai pegar do caractere na posição 9 até o 13, mas não inclui o 13

print(frase[9:21])
#Vai pegar do 9 ao 21, mas pegando so o da posição 20 (excluindo o 21)

print(frase[9:21:2])
#Ele vai de 9 até 21 pulando de 2 em 2

print(frase[:5])
# Vai começar do inicio ate o 5, excluindo a posição 5

print(frase[15:])
# Vai do 15 até o final (é bom caso vc nao saiba qual o ultimo caractere)

print(frase[9::3])
#Vai começar do 9 e ir ate o final, mas vai pulando de 3 em 3

print(len(frase))
#mostra o comprimento da frase, a quantidade de caracteres

print(frase.count('o'))
#Vai contar quantas vezes existe a letra O na frase

print(frase.count('o', 0, 13))
# vai contar quantos o tem da posição 0 à 13, excluindo a 13

print(frase.find('deo'))
#Vai te dizer a posição em que começa o deo

print(frase.find(' '))
#Vai contar a posição do primeiro espaço, eentao tecnicamente da pra vc saber a quantidade de letras da primeira palavra

print(frase.find('Android'))
#Se não existir ou nao for encontrado android vai retornar -1

print('Curso' in frase)
#Se existe sim ou não Curso na frase

print(frase.replace('Python','Android'))
#Vai caçar Python e substituir por android

print(frase.upper())
#A frase vai ficar toda em maiúscula

print(frase.lower())
#Deixa tudo em minúsculo 

print(frase.capitalize())
#Vai pegar a string toda deixar tudo minúsculo e só a primeira letra em maiúsculo

print(frase.title())
#Ele vai se basear na posição dos espaços e colocar todas as primeiras letras de palavras em maiúsculo e o resto em minúsculo


#divisão

print(frase.split())
#O split faz uma divisão dentro da string considerando onde tem espaço, ele pega os espaços e divide, divide curso, em, video, python. Basicamente ele separa e forma uma lista.

#Junção

print('-'.join(frase))
#Agora ele junta o que tava separado colocando esse -, se quiser que separe por espaço é só colocar espaço nas aspas.



