tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('O valor 3 não não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição ')
print(f'Os valores pares são ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
