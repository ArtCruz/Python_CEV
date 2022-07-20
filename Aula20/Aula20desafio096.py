def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}X{comp} pe de {a}m²')
    print()

    
print()
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)