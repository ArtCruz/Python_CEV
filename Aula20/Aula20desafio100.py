from random import randint
from time import sleep
soma = 0
def sorteia(lista):
    cont = 0
    for cont in range(0, 5):
        lista.append(randint(1, 10))
num = []
sorteia(num)
for values in num:
    if values % 2 == 0 :
        soma += values
print()
print('Sorteando 5 valores: ', end='')
for cont in range(0, 5):
    sleep(0.3)
    print(f'{num[cont]}', end=' ', flush=True)
    if cont == 4:
        print('PRONTO!')
print(f'Somando os \033[32m valores pares\033[m de {num}, temos {soma}')
print()