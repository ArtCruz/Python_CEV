n = input('Qual o seu nome completo? ')

print('\033[4m', n.upper(), '\033[m')

print('\033[4;34m', n.lower(), '\033[m')

print('\033[4;33m', len(n.replace(' ', '')), '\033[m')

div = n.split()
print('\033[4;32m', len(div[0]), '\033[m')
