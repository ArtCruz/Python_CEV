aluno = {}
aluno['nome'] = str(input('Nome: ')).capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-=' * 20 )
if aluno["media"] >= 7:
    aluno['situação'] = '\033[32mAprovado\033[m'
else:
    aluno['situação'] = '\033[31mReprovado\033[m'
for k, v in aluno.items():
     print(f'{k} é igual a {v}')