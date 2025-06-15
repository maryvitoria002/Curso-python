# Faça um programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
# Entrada = 3
# Saída = tabuada, quer ver a tabuada de qual valor? (quando digitar um negatico): tabuada encerrada

while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    if valor < 0:
        print("\nPrograma encerrado.")
        break
    for i in range (1, 11):
        print(f'{valor} x {i} = {valor*i}')
    