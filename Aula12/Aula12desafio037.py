num = int(input('Escolha um número inteiro qualquer: '))
ask = str(input('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: ''').capitalize())
if ask == '1':
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif ask == '2':
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif ask == '3':
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')
