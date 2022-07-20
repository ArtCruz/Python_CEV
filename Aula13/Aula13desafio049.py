num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{:.0f} X {} = {:.0f}'.format(num, c, num * c))
