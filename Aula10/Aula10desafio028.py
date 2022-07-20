from random import choice
n = int(input('Escolha um número inteiro entre 0 e 5: '))
if 0 <= n <= 5:
    print('\033[32mOK, seu número é valido\033[m')
else:
    print('\033[31mSeu número é inválido.\033[m ')
x = [0, 1, 2, 3, 4, 5]
y = choice(x)
if n == y:
    print('\033[4mEu também pensei no número {}\033[m'.format(y))
else:
    print('Eu pensei no número \033[4m{}\033[m'.format(y))
