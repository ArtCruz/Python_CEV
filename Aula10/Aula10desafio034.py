sal = float(input('\033[4mQuanto reais você ganha?\033[m '))
if sal <= 1250:
    x = (sal * 0.15) + sal
    print('O valor do seu \033[32mnovo salário\033[m é de \033[7;41m{:.2f}.\033[m'.format(x))
if sal > 1250:
    x = (sal * 0.10) + sal
    print('O valor do seu \033[32mnovo salário\033[m é de \033[7;41m{:.2f}.\033[m'.format(x))