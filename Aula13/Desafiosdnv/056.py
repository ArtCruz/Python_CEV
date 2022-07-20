media = 0
idadevelho = 0
mulnova = 0
velhonome = str
for d in range(1, 5):
    nome = str(input('O nome da {}ª pessoa: '.format(d))).strip().upper()
    idade = int(input('A idade da {}ª pessoa: '.format(d)))
    sexo = str(input('Sexo da {}ª pessoa: [M/F] '.format(d))).strip()
    print('-=' * 20)
    if d == 1:
        media = idade
    else:
        media = media + idade
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        velhonome = nome
    if sexo in 'Ff' and idade < 20:
        mulnova += 1
print('A média de idade desse grupo é de {} anos'.format(media / 4))
print('O homem mais velho se chama {}.'.format(velhonome))
print('Nesse grupo tem {} mulheres com menos de 20 anos.'.format(mulnova))


