times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
         'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')
print('Lista de times do Brasileirão: {}'. format(times))
print('=-=-=' * 60)
print('Os 5 primeiros colocados são: {}'.format(times[:6]))
print('=-=-=' * 60)
print('Os 4 últimos são: {}'.format(times[16:]))
print('=-=-=' * 60)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('O Grêmio está na {}ª posição'.format(times.index('Grêmio') + 1))  # Index = Procurar
''