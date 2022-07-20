from math import floor
num = float(input('Digite um número: '))
print('\033[4;45mO número {} tem parte inteira é {}\033[m'.format(num, floor(num)))
