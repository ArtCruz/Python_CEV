import random
w = input('Nome do \033[4;32mprimeiro\033[m aluno: ')
x = input('Nome do \033[4;32msegundo\033[m aluno: ')
y = input('Nome do \033[4;32mterceiro\033[m aluno: ')
z = input('Nome do \033[4;32mquarto\033[m aluno: ')
lista = [w, x, y, z]
escolhido = random.choice(lista)
print('\033[7;32mO aluno escolhido foi {}.\033[m'.format(escolhido))