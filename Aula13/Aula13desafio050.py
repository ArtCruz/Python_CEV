soma = 0
cont = 0
for c in range(1, 7):
    x = int(input('Digite o {} valor inteiro: '.format(c)))
    if x % 2 == 0:
        soma += x
        cont += 1
print('Você informou {} números PARES e a soma desses é {}.'.format(cont, soma))
