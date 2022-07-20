homens = 0
maiores = 0
mulheresmenos20 = 0
again = ' '
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        maiores += 1
    elif sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while again not in 'SN':
        again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if again == 'N':
        break
print(f'Esse grupo tem {maiores} pessoas maiores de 18 anos')
print(f'Esse grupo possui {homens} homens')
print(f'Esse grupo possui {mulheresmenos20} mulheres menores de 20 anos')
