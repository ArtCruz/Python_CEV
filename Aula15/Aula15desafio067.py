n = 0
while True:
    print('=-=' * 13)
    n = int(input('Digite um número para  ver sua tabuada: '))
    print('=-=' * 13)
    cont = 1
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} X {cont} = {n * cont}')
        cont += 1
print('Finalizando...')
