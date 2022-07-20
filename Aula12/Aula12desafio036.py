vc = float(input('Qual o valor da casa que você pretende comprar?'))
sal = float(input('Quanto você ganha por mês? '))
anos = float(input('Por quantos anos você pretende pagar a casa? '))
ps = sal * 0.3
emprest = ps * (anos * 12)
prest = vc / (anos * 12)
print('Para pagar uma casa de {} em {} anos a prestação será de {:.2f} e 30% do seu salário corresponde a {}, logo...'.format(vc, anos, prest, ps))
if vc <= emprest:
    print('\033[32mO seu crédito foi aprovado.\033[m ')
else:
    print('\033[31mO seu crédito foi negado.\033[m ')
