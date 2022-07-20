from datetime import date
ano = int(input('Que ano você nasceu?  '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade < 9:
    print('Esse atleta está na categoria MIRIM.')
elif 9 <= idade < 14:
    print('Esse atleta está na categoria INFANTIL.')
elif 14 <= idade < 19:
    print('Esse atleta está na categoria JUNIOR')
elif 19 <= idade < 20:
    print('Esse atleta está na categoria SÊNIOR')
elif 20 <= idade:
    print('Esse atleta está na categoria MASTER')
