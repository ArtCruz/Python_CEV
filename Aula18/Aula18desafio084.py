princ = []
temp = []
pesado = leve = 0
while True:
    temp.append(str(input('Qual o seu nome? ')).capitalize())
    temp.append(int(input('Qual o seu peso? ')))
    if len(princ) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Ao todo, {len(princ)} pessoas foram cadastradas')
print('O maior peso foi de {:.1f}kg. Peso de '.format(pesado), end='')
for p in princ:
    if p[1] == pesado:
        print(f'{p[0]}...', end='')
print('\nO menor peso foi de {:.1f}kg. Peso de '.format(leve), end='')
for p in princ:
    if p[1] == leve:
        print(f'{p[0]}...', end='') 