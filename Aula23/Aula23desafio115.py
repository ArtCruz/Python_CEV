from time import sleep


nomes = [
    'Ana Paula Vieira','Cláudio Mendonça', 'Gustavo Guanabara', 'Maria Clara Peixoto', 'Maurício Souza',
    'Nilce Pedrosa', 'Pedro Gonçalves', 'Rafael Albuquerque', 'Renata Soares'
]
idade = [
    '32', '18', '41', '65', '19', '43', '18', '38', '13'
]
def PessoasCadastradas():
    print('\033[m')
    print('--' * 25) 
    opç1 = 'PESSOAS CADASTRADAS'
    print(f'{opç1:^50}')
    print('--' * 25)
    linha = 0
    while True:
        if linha == len(nomes):
            break
        print(nomes[linha].ljust(25), end = '')
        if linha == len(idade):
            break
        print(idade[linha].rjust(20), 'anos')
        linha += 1
while True:
    print('--' * 25)
    menu = 'MENU PRINCIPAL'
    print(f'{menu:^50}')
    print('--' * 25)
    print('\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[36mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[36mSair do Sistema\033[m')
    print('--' * 25)
    sleep(1)
    while True:
        ok = False
        n = str(input('\033[33mSua Opção:\033[m '))
        if n.isnumeric():
            num = int(n)
            ok = True
        if ok and 1 <= num <= 3:
            break    
        else:
            print('\033[31mErro! Digite uma opção válida!\033[m')
    if num == 1:
        print('\033[32mCarregando', end='', flush=True)
        for c in range(3):
            if c < 3:
                sleep(1)
                print('.', end='', flush=True)
                c += 1
            else:
                sleep(1)
                print('.\033[m', flush=True)
        sleep(1)
        PessoasCadastradas()
    if num == 2:
        print('--' * 25)
        opç2 = 'NOVO CADASTRO'
        print(f'{opç2:^50}')
        print('--' * 25)
        n = str(input('Nome: ')).strip().title()
        str.split(str.capitalize(n))
        nomes.append(n)
        while True:
            ok = False
            i = str(input('Idade: ')).strip()
            if i.isnumeric():
                num = int(i)
                ok = True
            if ok:
                break    
            else:
                print('\033[31mErro! Digite um número inteiro válido!\033[m')
        idade.append(i)
        
    if num == 3:
        print('--' * 25) 
        sleep(0.25)
        print('         \033[32mSaindo do sistema', end='',flush=True)
        for c in range(3):
            if c < 3:
                sleep(1)
                print('.', end='', flush=True)
                c += 1
        sleep(1)
        print(' Até Logo!\033[m')
        print('--' * 25)
        break