n = input('Digite algo: ')

#Se o valor é numérico 
print(n.isnumeric())

#Se o valor é alfabético 
print(n.isalpha())

#Se o valor é alfanumerico
print(n.isalnum())

#Se está somente com letras maiúsculas
print(n.isupper())

#Se está somente com letras minúsculas
print(n.islower())

#Se ele tá com maiúsculas e minúsculas
print(n.istitle())

#Se ele pode ser impresso
print(n.isprintable())

#Se ele é um espaço
print(n.isspace())