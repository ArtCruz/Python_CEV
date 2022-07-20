from random import randint
count = 0
comp = randint(0, 10)
n = int(input('Escolha um número inteiro entre 0 e 10: '))
while not 0 <= n <= 10:
    n = int(input('\033[31mErro! Escolha um número inteiro entre 0 e 10: \033[m'))
while n != comp:
    if n < comp:
        print('\033[4:33mMais...Tente novamente\033[m')
    elif n > comp:
        print('\033[4:33mMenos...Tente novamente\033[m')
    print('-=' * 15)
    n = int(input('Escolha um número inteiro entre 0 e 5: '))
    count += 1
print('\033[32mParabéns, pensamos no mesmo número, você pensou no {} e eu no {}\033[m'.format(n, comp))
print('Você demorou \033[36m{}\033[m vezes para acertar'.format(count))
