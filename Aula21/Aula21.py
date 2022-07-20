help(input)           # Mesma coisa
print('-=' * 40)
print(input.__doc__)  # Mesma coisa
print('<->' * 30)
def contador(i, f, p):
    """ # Isso é uma DOCSTRING(manual da ajuda interativa)
    Faz uma contagem e mostra na tela:
    parametro i:início da contagem
    parametro f:fim da contagem
    parametro p:passo da contagem
    return:sem retorno
    """
    c = i 
    while c<= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
contador(2, 10,2 )
help(contador)  # Se eu usar um interactive help em uma função ela "não explica direito", por isso tem que usar as DOCSTRINGS
print('<->' * 30)
def somar(a, b, c = 0):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Arthur Espindola da Cruz
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4) #Como o c nao receberia um parametro o c = 0 faz com que quando este não tenha um valor ele receba 0(Parametro opcional)
help(somar)
print('<->' * 30)
def teste():
    x = 8 # "x" tem um escopo local pois está dentro da def
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2 # Já "n" tem um escopo global pois consegue ser atribuída em qualquer programa
print(f'No programa principal, vale {n}')
teste()
print('No programa principal, x vale {x}')
print('<->' * 30)
def teste(b):
    global a # Programa faça com que o "a global" receba a "info" que o "a local" receberia 
    a = 8   # Existe uma variável de escopo local que só serve para dentro dessa função
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 # Existe uma váriavel de escopo global, com o mesmo "nome"
teste(a)  # O programa vai criar uma cópia desse "a" mas vai chamar de "b" pq esse é o parametro da função  
print(f'A fora vale {a}')
print('<->' * 30)
def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s # Ele vai retornar o valor de "s" para o que vier antes de somar()
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')