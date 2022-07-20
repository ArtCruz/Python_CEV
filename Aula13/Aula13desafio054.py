from datetime import date
cont = 0
for c in range(1, 8):
    x = int(input('Data de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - x >= 18:
        cont += 1
print('Desse grupo {} já atingiram a maioridade.'.format(cont))
print('Desse grupo {} ainda não atingiram a maioridade.'.format(7 - cont))
