fra = str(input('Me diga uma frase e direi se é um PALÍNDROMO: ')).strip().upper()
x = fra.replace(' ', '')
if x == x[::-1]:
    print('\033[32mA frase {} é um PALÍNDROMO\033[m'.format(fra))
else:
    print('\033[31mA frase {} não é um PALÍNDROMO.\033[m'.format(fra))
