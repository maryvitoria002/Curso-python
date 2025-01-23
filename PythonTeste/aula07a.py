nome = input('Qual é o seu nome? ')
print ('Prazer em te conhecer {}!'.format(nome))

#Se eu coloco dentro das chaves algum valor, como {:20} o resultado ocupará 20 espaços, e dessa forma é possível fazer alinhamentos.

print ('Prazer em te conhecer {:20}!'.format(nome))


#Alinhando o resultado à esquerda (que é já o padrão) com 20 espaços:

print ('Prazer em te conhecer {:<20}!'.format(nome))

#Alinhando o resultado à direita com 20 espaços:

print ('Prazer em te conhecer {:>20}!'.format(nome))

#Alinhando o resultado no centro com 20 espaços:

print ('Prazer em te conhecer {:^20}!'.format(nome))

#Alinhando o resultado no centro com 20 espaços sendo preenchidos pelo '=':

print ('Prazer em te conhecer {:=^20}!'.format(nome))

