# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no fim do jogo.
# entrada = diga um valor: 6
# voce quer par ou impar [P/I]: I

# saida = voce jogou 6 e o computador jogou 10. Total de 16 deu par
# voce perdeu
# =+=+=+=+
# game over voce venceu 0 vezes

# caso ganhe
# entrada = diga um valor: 8
# # voce quer par ou impar [P/I]: P

# # saida = voce jogou 8 e o computador jogou 2. Total de 10 deu par
# voce venceu! 
# vamos jogar novamente...
# diga um valor:
# (so para quando vc perde)
import random
i = 0
while True:
    valor = int(input("Digite um valor: "))
    escolha = input("voce quer par ou impar [P/I]: ").upper()
    comp = random.randint(0, 10)
    soma = comp + valor
    if soma % 2 ==0:
        print(f'voce jogou {valor} e o computador jogou {comp}. Total de {soma}, deu par')
        if escolha == 'P':
            print('Você venceu!!')
            i +=1
        elif escolha =='I':
            print(f'Você perdeu, ganhou {i} vezes!!')
            break
        else:
            print('Não foi essa opção que foi dado')
            continue
    else: 
        print(f'voce jogou {valor} e o computador jogou {comp}. Total de {soma}, deu ímpar')
        if escolha == 'I':
            print('Você venceu!!')
            i +=1
        elif escolha =='P':
            print(f'Você perdeu, ganhou {i} vezes!!')
            break
        else:
            print('Não foi essa opção que foi dado')
            continue
    
