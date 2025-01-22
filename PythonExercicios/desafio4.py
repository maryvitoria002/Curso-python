#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

n = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(n))
 
print('é numérico? ', n.isnumeric())
 
print('é alfabético ?', n.isalpha())
 
print('é alfanumerico? ', n.isalnum())

print('está somente com letras maiúsculas? ', n.isupper())

print('está somente com letras minúsculas? ', n.islower())

print('pode ser impresso?', n.isprintable())

print('é um espaço? ', n.isspace())