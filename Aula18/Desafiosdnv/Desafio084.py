princ = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Qual o seu nome? ')).capitalize())
    temp.append(int(input('Qual o seu peso? ')))
    if len(princ) == 0:
        mai = temp[1]
        men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]    
    princ.append(temp[:])
    temp.clear()
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Ao todo, {len(princ)} foram cadastradas')
print(f'O MAIOR peso cadastrados foi {mai}kg. Peso de ', end='')
for b in princ:
    if b[1] == mai:
        print(f'{b[0]}...',end ='')
print(f'\nO MENOR peso cadastrados foi {men}kg. Peso de ', end='')
for s in princ:
    if s[1] == men:
        print(f'{s[0]}...', end='')