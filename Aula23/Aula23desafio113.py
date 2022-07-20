def LeiaInt(msg):
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break    
    return num
n = LeiaInt('Digite um número inteiro: ')
def LeiaFloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input(msg))
            if (n * 1) / 1 == n:
                valor = float(n)
                ok = True
        except:
            print('\033[31mErro! Digite um número real válido.\033[m')
        if ok:
            break
    return valor
r = LeiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número real {r}')
