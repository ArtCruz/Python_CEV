soma = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}.'. format(cont, soma))