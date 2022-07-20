nome = str(input('Qual o seu nome? ')).strip()
n = nome.split()
print('Seu \033[1;32mprimeiro\033[m nome é \033[4m{}\033[m ' .format(n[0]))
print('Seu \033[1;31múltimo\033[m nome é \033[4m{}\033[m'.format(n[len(n)-1]))
