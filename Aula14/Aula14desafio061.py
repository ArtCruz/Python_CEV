print('=-=' * 10)
print('Calculador de PA')
print('=-=' * 10)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
cont = 0
pa = num + raz
while cont < 9:
    if cont == 0:
        print(num, end=' -> ')
    pa = num + raz
    print(pa, end=' -> ')
    num = pa
    cont += 1
print('FIM')