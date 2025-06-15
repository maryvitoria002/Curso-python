# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

print ("="*40)
print ("      10 PRIMEIROS TERMOS DE UMA PA")
print ("="*40)

a1= int(input("Digite o 1º termo: "))
r= int(input("Digite a razão: "))
    
i = 0        # quantos termos já mostrei
total  = 0        # quantos termos devo mostrar ao todo
mais   = 10       # começa exibindo 10

while mais != 0:
    total += mais                 
    while i < total:           # exibe até alcançar o total
        print(a1, end=' → ')
        a1 += r
        i  += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer? (0 p/ encerrar) '))
print(f'\nProgressão encerrada com {total} termos mostrados.')
