print('==' * 20)
print('Os 10 Primeiros Termos de um PA')
print('==' * 20)
num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = num + (10 - 1) * raz
for c in range(num, dec + raz, raz):
    print(c)
print('Acabou')
