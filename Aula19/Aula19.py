dados = []
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados)
print('-=-=' * 20)
dados = {}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #Seria o append das listas
print(dados)
del dados['idade']
print(dados)
print('-=-=' * 20)
filme = {
    'titulo':'Star Wars',
    'ano':1977, 
    'diretor':'George Lucas'
}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f'O {k} é {v}')
print('-=-=' * 20)
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
pessoas['peso'] = 98.5
pessoas['nome'] = 'Leandro'
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ')
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=-=' * 20)
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-=-=' * 20)
estado = {}
nation = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    nation.append(estado.copy()) # Seria o nation.append(estado[:]) pq esse não funciona
print(nation)
for e in nation:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')