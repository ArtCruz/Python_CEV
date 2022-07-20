pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
pa = 0
for n in range(1, 10):
    if n == 1:
        print(pt)
        pa = pa + (pt + raz)
        print(pa)
    else:
        pa = pa + raz
        print(pa)
print('ACABOU!')