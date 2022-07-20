tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    esc = ''
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente. ', end='')
    print(f'Você digitou o número {tupla[num]}')
    esc = str(input('Aperte "N" para : ')).strip().upper()[0]
    if esc == 'N':
        break
print('Volte Sempre!')
