val = ''
maior = menor = 0
lista = []
for cont in range(0,5):
    val = (int(input(f'Digite um valor para a posição {cont}:')))
    lista.append(val)
    if cont == 0:
        maior = menor = val
    else:
        if maior < val:
            maior = val
        if menor > val:
            menor = val
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O MAIOR valor digitado foi {maior} na posição ', end= '')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}...', end= '')
print(f'\nO MENOR valor digitado foi {menor} na posição ', end= '')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}...', end= '')