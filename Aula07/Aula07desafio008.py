d = float(input('Quantos metros são? '))
print('\033[4mQue é equivalente a {:.0f} \033[7;31mcentímetros\033[m\033[4m e {:.0f} \033[7;34mmilímetros\033[m'.format(d*100, d*1000))
