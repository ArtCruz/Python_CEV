l1 = float(input('Lado \033[34mUM\033[m: '))
l2 = float(input('Lado \033[35mDOIS\033[m: '))
l3 = float(input('Lado \033[36mTRÊS\033[m: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('\033[4;32mÉ possível\033[m formar um \033[33mtriângulo\033[m com os lados {},{} e {}!'.format(l1, l2, l3))
else:
    print('\033[4;31mNão é possível\033[m foramr um \033[33mtriângulo\033[m com estas medidas')
