from random import shuffle
n1 = input('\033[4;35mPrimeiro aluno:\033[m ')
n2 = input('\033[4;35mSegundo aluno:\033[m ')
n3 = input('\033[4;35mTerceiro aluno:\033[m ')
n4 = input('\033[4;35mQuarto aluno:\033[m ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[4mA ordem de apresentação será:', '\033[1;35m', lista, '\033[m')
