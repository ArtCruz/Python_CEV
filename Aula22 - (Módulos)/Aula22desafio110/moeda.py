def metade(n, formato = False):
    res = n / 2
    return res if formato is False else moeda(res)

def dobro(n, formato = False):
    res = n * 2
    return res if formato is False else moeda(res)

def aumentar(n, formato=False):
    res = n * 1.80
    return res if formato is False else moeda(res)

def reduzir(n, formato = False):
    res = n * 0.65
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(n):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{n}')
    print(f'Dobro do Preço: \t{moeda(dobro(n))}')
    print(f'Metade do Preço: \t{moeda(metade(n))}')
    print(f'80% de aumento: \t{moeda(aumentar(n))}')
    print(f'35% de redução: \t{moeda(reduzir(n))}')
    print('-' * 30)