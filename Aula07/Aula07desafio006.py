n = int(input('Digite um número: '))
print('\033[7;31;42mSeu dobro é {},\033[m \033[7;32;43mseu triplo é {} e\033[m \033[7;33;44msua raiz quadrada é {:.0f}\033[m'.format(n*2, n*3, n**(1/2)))
