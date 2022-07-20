def factorial(n, show = False):
    """
    CALCULANDO O FATORIAL:
    param n: número escolhido pelo usuário
    param show: um valor boleano que mostrará ou não a conta por extenso
    return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ',end ='')
            else:
                print(' = ', end ='')
        f *= c
    return f
print(factorial(9, show=True))
help(factorial)