def SistPython():
    print('\033[7;32;40m~' * 30)
    print('   Sistema de Ajuda PyHELP    ')
    print('~' * 30)
    print('\033[m')

def Which(msg):
    print('\033[30;44m~' * 50)
    print(f'         Acessando o manual do comando "{word}"        ')
    print('~' * 50)
    print('\033[m')

def Manual():
    print('\033[7;38m')
    print(help(word))
    print('\033[m')

while True:
    SistPython()
    word = str(input('Função ou Biblioteca > '))
    Which(word)
    Manual()
    end = str(input('Quer continuar? [S/N]')).upper()[0]
    while True:
        if end in 'S/N':
            if end == 'S':
                break
        else:
            print('\033[31mERRO! Opção inválida, use \033[mS \033[31mou \033[mN\033[m')
    
