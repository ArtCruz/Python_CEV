nome = str(input('Qual é o seu nome? ').capitalize())
if nome == 'Arthur':
    print('Mas que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil, {}.'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino :)')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))
