#Crie o programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem final de acordo: média abaixo de 5.0: reprovado, média entre 5 e 6.9: em recuperação. Média 7 ou superior: aprovado.

n1 = float(input(('Qual a primeira nota do aluno? ')))
n2 = float(input(('Qual a segunda nota do aluno? ')))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media} e voce foi reprovado')
elif media > 5:
    print(f'Sua média foi {media} e voce foi aprovado')
else:
    print(f'Sua média foi {media} e voce tá de recuperação')