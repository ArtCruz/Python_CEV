lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 not in lista:
    print('O número 5 não está na lista')
else:
    print('O número 5 foi encontrado na posição ', end='')
    for pos, n in enumerate(lista):
        if n == 5:
            print(f'{pos}...', end='')