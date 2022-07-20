def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumentar(n):
    return n * 1.10

def reduzir(n):
    return n * 0.87

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')