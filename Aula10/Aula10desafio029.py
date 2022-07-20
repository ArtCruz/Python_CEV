vel = float(input('Qual a velocidade do carro em km/h? '))
x = (vel - 80) * 7
print('-=-' * 20)
if vel > 80:
    print('\033[31mVocê excedeu o limite de 80km/h.\033[m \n'
          'Você deverá pagar uma multa de \033[31m{:.2f} reais.\033[m'.format(x))
else:
    print('\033[4;32mVocê não foi multado.\033[m')
