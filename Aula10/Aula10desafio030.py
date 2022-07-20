num = int(input('Me diga um número: '))
if (num % 2) == 0:
    print('\033[4mO número \033[7m{}\033[m\033[4m é \033[31mPAR.\033[m'.format(num))
else:
    print('\033[4mO número \033[7m{}\033[m\033[4m é \033[34mIMPAR.\033[m'.format(num))
