def metade(n, formato = False):
    res = n / 2
    return res if formato is False else moeda(res)

def dobro(n, formato = False):
    res = n * 2
    return res if formato is False else moeda(res)

def aumentar(n, formato=False):
    res = n * 1.10
    return res if formato is False else moeda(res)

def reduzir(n, formato = False):
    res = n * 0.87
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')