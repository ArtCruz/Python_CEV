jogador = {}
gols = []
c = 1
total = t = 0
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    while c != partidas + 1:
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        c += 1
    jogador['Gols'] = gols
    jogador['Total de Gols'] = sum(gols)
    break
print('-=' * 40)
print(jogador)
print('-=' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 40)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
while True:
    print(f'    => Na partida {t}, fez {gols[t]} gols.')
    t += 1
    if t == partidas:
        break
print(f'Foi um total de {jogador["Total de Gols"]} gols.')
print('-=' * 40)
print('\033[31mVolte Sempre\033[m')