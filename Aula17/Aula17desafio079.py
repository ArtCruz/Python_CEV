lista = []
while True:
    val = int(input('Digite um valor: '))
    if val not in lista:
        lista.append(val)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não será adicionado')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Você digitou os valores{sorted(lista)}')