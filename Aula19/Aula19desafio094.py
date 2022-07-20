pessoas = []
indiv = {}
soma = 0
while True:
    indiv.clear()
    indiv['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        indiv['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if indiv['Sexo'] in 'MF':
            break
        print('\033[31mERRO! Por favor, digite apenas M ou F.\033[m')
    idade = int(input('Idade: '))
    indiv['Idade'] = idade
    soma += idade
    pessoas.append(indiv.copy())
    while True:
        cnt = str(input('Quer continuar? [S/N] ')).upper()[0]
        if cnt in 'SN':
            break
        print('\033[31mERRO! Por favor, digite apenas S ou N.\033[m')
    if cnt == 'N':
        break
print('-=' * 40)
print(f'A) O grupo tem {len(pessoas)} pessoas.')
print(f'B) A média de idade é de {(soma)/len(pessoas):.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end= '' )
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=', ')
print()
print('A lista de pessoas que estão acima da média: ', end='')
print()
for p in pessoas:
    if p['Idade'] > soma/len(pessoas):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\033[33m<< ENCERRADO >>\033[m')