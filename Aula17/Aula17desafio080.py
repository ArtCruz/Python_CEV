lista = []
for cont in range (0,5):
    num = int(input(f'Digite o {cont} valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print('-=' * 30)
print(f'Os valors digitados em ordem foram {lista}')