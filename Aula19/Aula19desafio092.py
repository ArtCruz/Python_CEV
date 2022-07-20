from datetime import date
pessoa = {}
while True:
    pessoa['Nome'] = str(input('Nome: ')).capitalize()
    nasc = int(input('Ano de Nascimento: '))
    pessoa['Idade'] = date.today().year - nasc
    cart = int(input('Carteira de Trabalho (0 não tem): '))
    if cart == 0:
        pessoa['CTPS'] = 'Não possui'
        break
    else:
        pessoa['CTPS'] = cart
        ano = int(input('Ano de Contratação: '))
        pessoa['Ano de Contratação'] = ano
        pessoa['Salário'] = float(input('Salário: '))
        pessoa['Aposentadoria'] = (ano + 35) - nasc
    break
print('-=' * 20)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')
