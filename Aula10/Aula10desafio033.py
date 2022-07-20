n1 = float(input('Me diga um número: '))
n2 = float(input('Me diga um número: '))
n3 = float(input('Me diga um número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[34mmaior\033[m número é \033[4m{:.0f}\033[m'.format(maior))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O \033[36mmenor\033[m número é \033[4m{:.0f}\033[m'.format(menor))
