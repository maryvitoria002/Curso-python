#crie um programa que faça o computador jogar pedra papel tesoura com você.

from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print ('-=' * 11)

if jogador == 0 or jogador == 1 or jogador == 2:
    print (f'O computador escolheu {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 11)

    if itens[computador] == itens[0] and itens[jogador] == itens[0]:
        print ("Empatou!!")

    elif itens[computador] == itens[0] and itens[jogador] == itens[1]:
        print ("Você ganhou!!")
        
    elif itens[computador] == itens[0] and itens[jogador] == itens[2]:
        print ("Você perdeu!!")

    elif itens[computador] == itens[1] and itens[jogador] == itens[0]:
        print ("Você perdeu!!")

    elif itens[computador] == itens[1] and itens[jogador] == itens[1]:
        print ("Empatou!!")

    elif itens[computador] == itens[1] and itens[jogador] == itens[2]:
        print ("Você ganhou!!")

    elif itens[computador] == itens[2] and itens[jogador] == itens[0]:
        print ("Você ganhou!!")

    elif itens[computador] == itens[2] and itens[jogador] == itens[1]:
        print ("Você perdeu!!")

    elif itens[computador] == itens[2] and itens[jogador] == itens[2]:
        print ("Empatou!!")
   
else:
     print ('Deu ruim tropinha, escolhe a alternativa certa man, presta atenção man')

    



