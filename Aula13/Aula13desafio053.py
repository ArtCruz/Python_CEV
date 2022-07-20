fra = str(input('Me diga uma frase eu lhe direi se é um PALÍNDROMO ou não: ')).strip().upper()
x = fra.replace(" ", "")
frain = x[::-1]
if x == frain:
    print('\033[34mA frase {} é um palíndromo.'.format(fra))
else:
    print('\033[31mA frase {} não é um palíndromo.'.format(fra))
