from random import randint
menor = 11
maior = 0
cont = ''
for cont in range(1, 6):
    x = randint(0, 10)
    if cont == 0:
        x = maior = menor
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    print('O {}º número sorteado foi: {}'.format(cont, x))
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#   print(f'{n} ', end='')
# print('\nO maior valor sorteado foi {max(numeros)})
# print('O menor valor sorteado foi {min(numeros)})

