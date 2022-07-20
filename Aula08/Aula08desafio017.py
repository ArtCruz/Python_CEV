from math import sqrt
co = float(input('Qual o comprimento do \033[31mcateto oposto?\033[m '))
ca = float(input('Qual o comprimento do \033[34mcateto adjacente?\033[m '))
x = ca*ca + co*co
hip = sqrt(x)
print('\033[4mO valor da hipotenusa é\033[m \033[35m{}\033[m'.format(hip))
