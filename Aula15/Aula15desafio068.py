from random import randint
print('=-=' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 13)
vitorias = 0
while True:
    computador = randint(0, 10)
    num = int(input('Diga um valor: '))
    esc = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()
    print('---' * 15)
    if esc == 'P':
        esc = 'PAR'
    if esc == 'I':
        esc = 'ÍMPAR'
    soma = num + computador
    valor = 0
    if soma % 2 == 0:
        valor = 'PAR'
    else:
        valor = 'ÍMPAR'
    print(f'Você jogou {num} e o computador {computador}. Total de {soma} deu {valor}')
    print('---' * 15)
    if esc == valor:
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
        print('---' * 15)
    elif esc != valor:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {vitorias} vezes')
        break
print('Finalizando...')
