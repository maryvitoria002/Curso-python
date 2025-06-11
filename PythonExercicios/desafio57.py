# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto 

sexo = 'e'
while True:
    sexo = str(input("Digite seu sexo [M/F]: ").upper()).strip()
    if sexo == 'M' or sexo == 'F':
        break
    print("Dados inválidos.")
print(f"Registrado com sucesso")

