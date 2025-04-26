#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

niv = int(input('Que ano você nasceu? '))
idade =  2025 - niv

if idade > 18:
    print(f'Meu mano já passou do tempo, ta atrasado {idade - 18} anos')

elif idade < 18:
    print(f'Tá cedo rapaz, falta {18 - idade} anos ainda')

else:
    print('Tá na hora man')
    