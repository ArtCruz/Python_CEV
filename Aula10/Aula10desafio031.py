d = float(input('Qual a distância da sua viagem? '))
p1 = d * 0.5
p2 = d * 0.45
if d < 200:
    print('O valor da sua viagem será de \033[33m{:.2f} reais.\033[m'.format(p1))
else:
    print('O valor da sua viagem será de \033[33m{:.2f} reais.\033[m'.format(p2))
print('\033[4;34mTENHA UMA BOA VIAGEM!!!\033[m')