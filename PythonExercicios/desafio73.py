# Cria uma tupla praanchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordam da colocação. Depois mostra:

# A) Apenas os 5 primeiros colocados.

# B) Os últimos 4 colocados da tabala.

# C) Uma lista com os times em ordem alfabética.

# D) Em que posição na tabala astá o time da Vasco.

times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Fluminense', 'Botafogo', 'Bahia', 'Mirassol', 'Atlético-MG', 'Ceará SC', 'Corinthians', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco da Gama', 'EC Vitória', 'Fortaleza', 'Santos', 'Juventude', 'Sport Recife')

print("Os 5 primeiros times são: ")
for i in range (0, 5):
    print(times[i], end=', ')

print("\n\n Os 4 últimos times são: ")
for i in range (-4, 0):
    print(times[i], end=', ')

print("\n\n Times na ordem alfabética: ")
print (sorted(times), end='')

print(f"\n\n O Vasco está na {times.index('Vasco da Gama')+ 1}º posição")