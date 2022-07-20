from datetime import date
maior = 0
menor = 0
for n in range(1, 8):
    x = int(input('Ano de nascimento da {}ª pessoa: '.format(n)))
    if (date.today().year - x) >= 18:
        maior += 1
    else:
        menor += 1
print('Desse grupo {} já são de maior e {} ainda são de menor'.format(maior, menor))
