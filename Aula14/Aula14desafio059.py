from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
op = 0
while op != 5:
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    op = int(input('>>>>>Qual a sua opção? '))
    print('=-=' * 13)
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('Os dois valores são iguais')
    elif op == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
print('Finalizando...')
sleep(1)
