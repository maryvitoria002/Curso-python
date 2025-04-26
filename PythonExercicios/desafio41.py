#A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade- ate 9 anos:mirim, ate 14 anos: infantil, ate 19 anos: junior, ate 20 anos: senior, acima: master.

ano = int(input('Qual ano você nasceu? '))
idade = 2025 - ano

if idade <= 9:
    print("Cé é mirim Zé")
elif idade <= 14:
    print("Cé é infantil Zé")
elif idade <= 19:
    print("Cé é junior Zé")
elif idade <= 20:
    print("Cé é senior Zé")
else:
    print("Cé é master Zé")
