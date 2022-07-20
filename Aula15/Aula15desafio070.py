total = totmil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Qual o nome do produto? ')).capitalize().strip()
    preco = float(input('Preço: R$'))
    cont += 1
    rep = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    while rep not in 'SN':
        rep = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if rep == 'N':
        break
print(f'O total da compra foi de R${total:.2f}')
print(f'Nessa compra existem {totmil} valores maiores de R$1000')
print(f'O produto mais barato é a/o {barato}')
