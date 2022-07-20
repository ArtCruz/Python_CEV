from datetime import date
ano = int(input('Em que ano você nasceu? '))
sexo = int(input('''[ 1 ] para sexo MASCULINO
[ 2 ] para sexo FEMININO
Me diga o seu sexo: '''))
year = date.today().year
x = (year - ano)
if sexo == 1 and x < 18:
    print('''Você não precisa se alistar esse ano.
Ainda falta {} anos para seu alistamento.
Seu alistamento será em {}.'''.format(18-x, ano + 18))
elif sexo == 1 and x == 18:
    print('''Quem nasceu em {} tem 18 anos em {}.
Você tem que se alistar IMEDIATAMENTE! '''.format(ano, year))
elif sexo == 1 and x > 18:
    print('''Já passou o ano do seu alistamento.
Supostamente você se alistou a {} anos atrás.
Seu alistamento foi em {}.'''.format(x-18, ano + 18))
else:
    print('Por ser do sexo FEMININO você não precisa participar do alistamento militar obrigatório.')
