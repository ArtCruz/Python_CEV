from random import randint
num = randint(1, 61)
lista = []
jogos = []
print('--' * 20)
print('          JOGUE NA MEGA SENA')
print('--' * 20)
quant = int(input('Quantos jogos você quer criar? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 5, f'SORTEANDO {quant} JOGOS', '-=' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
print('-=' * 7, 'BOA SORTE!', '-=' * 7)