l1 = float(input('LADO UM: '))
l2 = float(input('LADO DOIS: '))
l3 = float(input('Lado TRÊS: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('\033[34mÉ possível formar um triângulo com as medidas {}, {} e {}.\033[m'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('Esse triângulo é EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Esse triângulo é ISÓSCELES.')
    elif l1 != l2 != l3 != l1:
        print('Esse é um triângulo ESCALENO')
else:
    print('\033[31mNão é possível foramr um triângulo com essas medidas.\033[m')
