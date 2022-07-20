n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n O produto é {}, \n A divisão é {:.3f}'.format(s, m, d), end=' ')
# {.3f} serve para 3 casas dps da ,
# , end='' serve para não ter um novo "paragrafo"
print('Divisão inteira {}, e potência {}'.format(di, e))
