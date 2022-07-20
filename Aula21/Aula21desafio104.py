def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break    
    return valor
n = LeiaInt('Digite um número inteiro: ')
print(f'Você digitou o número inteiro {n}')