n = int(input('Digite um número: '))
print('\033[4;46mAnalisando o número {}...\033[m'.format(n))
u = n // 1 % 10
print('\033[30mUnidades: {}\033[m'.format(u))
w = (n // 1 % 100 - u)
d = w/10
print('\033[31mDezenas: {:.0f}\033[m'.format(d))
x = (n // 1 % 1000 - (u + w))
c = x / 100
print('\033[32mCentenas: {:.0f}\033[m'.format(c))
y = (n // 1 - (x + w + u))
m = y / 1000
print('\033[33mUnidades de Milhar: {:.0f}\033[m'.format(m))
