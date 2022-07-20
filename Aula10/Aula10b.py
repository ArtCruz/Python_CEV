n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.2f}, logo... '.format(m))
if m >= 7:
    print('Você passou na matéria: ')
else:
    print('Você não passou na matéria')
