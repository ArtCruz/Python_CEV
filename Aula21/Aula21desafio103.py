def futebol(name = '<desconhecido>', score = 0):
    print(f'O jogador {name} fez {score} gol(s) no campeonato.')
n = str(input('Nome do Jogador: ')).capitalize()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    futebol(score=g)
else:
    futebol(n, g)
