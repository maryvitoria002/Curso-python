#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas as letras minusculas, quantas letras ao todo (Sem considerar os espaços) e quantas letras tem o primeiro nome

nome = str(input('Qual seu nome? ')).strip()

print(f"""Seu nome em maiúsculo: {nome.upper()}
Seu nome em minúsculo: {nome.lower()}
Seu nome tem {len(nome)-nome.count(' ')} caracteres
E seu primeiro nome tem {nome.find(' ')} letras.""")

nome1 = nome.split()
print(f'De forma alternativa, seu primeiro nome é {nome1[0]} e tem {len(nome1[0])} letras')

