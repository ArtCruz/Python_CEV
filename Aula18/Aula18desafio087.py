matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
pares = []
tercol = []
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if c == 2:
            tercol.append(matriz[l][c])
        if l == 1 and c == 0:
            mai = matriz[l][c]
        elif l == 1:
            if matriz[l][c] > mai:
                mai = matriz[l][c]
print('-=' * 25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {sum(tercol)}')
print(f'O maior valor da segunda linha é {mai}')
