print('==' * 15)
print('{:-^30}'.format(' BANCO PYTHON '))
print('==' * 15)
notas50 = notas20 = notas10 = notas1 = 0
valor = int(input('Qual o valor que será sacado? R$'))
while valor != 0:
    while valor >= 50:
        valor = valor - 50
        notas50 += 1
    if valor >= 20:
        while valor >= 20:
            valor = valor - 20
            notas20 += 1
    if valor >= 10:
        while valor >= 10:
            valor = valor - 10
            notas10 += 1
    if valor >= 1:
        while valor >= 1:
            valor = valor - 1
            notas1 += 1
    break
if notas50 >= 1:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 >= 1:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 >= 1:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 >= 1:
    print(f'Total de {notas1} cédulas de R$1')
print('==' * 15)
print('Volte Sempre')
