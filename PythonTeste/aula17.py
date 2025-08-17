# LISTAS

# Diferente das tuplas, as listas são mutáveis, e são representadas por '[]'
lista = ["Mary", "Bruno", "Tom"]
print(lista[2])
# Para adicionar um elemento a uma lista, usa-se

lista.append("Maete")
print(lista)

# Para adicionar um elemento em uma posição específica se usa insert, e coloca entre parenteses o indice e o elemento

lista.insert(0, "Auguta")
print(lista)

# Para apagar tem muitas formas, del, pop (normalmente elimina o ultimo) e remove
del lista[0]
print(lista)

# Mas vc tbm pode colocar um indice no pop
lista.pop()

# No caso do remove vc nao coloca o indice, e sim o proprio elemento
if 'Mary' in lista:
    lista.remove('Mary')
print(lista)    

# Pra adicionar os valores numa lista de 4 a 11

Valores = list(range(4,11))

# Pra colocar os valores em ordem usamos sort
numeros = [4, 7, 1, 3, 0, 2]
numeros.sort()
print(numeros)

# E se eu quiser o inverso
numeros.sort(reverse=True)
print(numeros)

# Pra descobrir quantos elementos tem em uma lista de usa len
len(numeros)

