soma = cont = 0
num = int(input('''Caso queira fechar o programa digite "999"
Digite um número:'''))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('A soma dos {} valores digitados(desconsiderando o flag) foi {}'.format(cont, soma))
