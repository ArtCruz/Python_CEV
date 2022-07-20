n1 = int(input('\033[0;32;40mDigite um número:\033[m '))
n2 = int(input('\033[0;32;40mDigite outro número:\033[m '))
s = n1 + n2
print('A soma de \033[0;32;40m{}\033[m mais \033[0;32;40m{}\033[m é igual a \033[7;32;40m{}\033[m'.format(n1, n2, s))
