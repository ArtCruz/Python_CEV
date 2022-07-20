num = int(input('Diga um número inteiro para ver sua tabuada: '))
for n in range(1, 11):
    print('{:.0f} X {:.0f}: {:.0f}'.format(num, n, num * n))
