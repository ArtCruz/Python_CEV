x = float(input('\033[7;33mQual a largura da parede?\033[m '))
y = float(input('\033[7;35mQual a altura da parede?\033[m '))
z = x * y
print('\033[7;33mA área da parede é de {:.2f} e \033[m\033[7;35mvocê precisará de {:.2f} litros de tinta\033[m'.format(z, z/2))
