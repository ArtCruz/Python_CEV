tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
        print('{}'.format(c), end='')
    else:
        print('\033[31m', end=' ')
        print('{}'.format(c), end='')
print('\nO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('\033[32mO número {} é PRIMO.'.format(num))
else:
    print('\033[31mO número {} não é PRIMO'.format(num))