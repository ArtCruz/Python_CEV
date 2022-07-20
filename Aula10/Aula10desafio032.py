from datetime import date
ano = int(input('Que ano você quer analisar? Digite 0 se quiser analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[4m{}\033[m \033[32mé\033[m bissexto.'.format(ano))
else:
    print('O ano \033[4m{}\033[m \033[31mnão é\033[m bissexto.'.format(ano))
