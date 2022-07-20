num = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
cont = 1
media = num
maior = menor = num
while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    media = (media + num)
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media /= cont
print('A média de todos os elementos foi {:.2f}'.format(media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('Finalizando...')
