valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('=-=' * 20)
a = [2, 3, 4, 7]
b = a[:] # Fazer com que B receba TODOS os elementos de A - CÓPIA
# b = a as listas se "conectam" e ao mudar o b eu mudo o a - LIGAÇÃO
b [2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
