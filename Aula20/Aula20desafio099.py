from time import sleep
def valores(*num):
    maior = 0
    print('-=' * 40)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush= True)
        sleep(0.3)
    tam = len(num)
    print(f'Foram informados {tam} valores ao todo.')
    if tam == 0:
        print('O maior valor foi 0.')
    else:
        maior = max(num)
        print(f'O maior valor informado foi {maior}.')
valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores(-10, -8, -2, -4)
valores()
print() 