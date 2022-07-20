players = []
jogador = {}
gols = []
while True:
    c = 1
    gols.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    while c != partidas + 1:
        gols.append(int(input(f'    Quantos gols na partida {c}? ')))
        c += 1
    jogador['Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    players.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO! Digite apenas S ou N\033[m')
    if resp == 'N':
        print('<->' * 30)
        break
    else:
        print('-=' * 40)
print('cod   ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_ _ ' * 15)
for k, v in enumerate(players):
    print(f'{k:>4}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    show = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if show == 999:
        break
    if show >= len(players):
        print(f'\033[31mERRO! Não existe jogador com código\033[m {show}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {players[show]["Nome"]}')
        for i, g in enumerate(players[show]['Gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('--' * 20)
print('<->' * 30)