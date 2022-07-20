soma = 0
somanum = 0
for n in range(1, 501):
    if n % 3 == 0 and n % 2 != 0:
        if n == 3:
            soma = soma + n
            somanum = somanum + 1
        else:
            soma = soma + n
            somanum = somanum + 1
print('A soma dos {} valores é {}.'.format(somanum, soma))
