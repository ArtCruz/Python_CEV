def mude():
    print('<->' * 30)
print('-' * 30)
print('Curso em Vídeo')
print('-' * 30)
def lin():
    print('-' * 30)
lin()
print('Curso em Vídeo')
lin()
mude()
def mensagem(msg):
    lin()
    print(msg)
    lin()
mensagem(f'       CURSO EM VÍDEO')
mude()
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
soma(4, 5)
soma(b=3, a=9)
soma(2, 1)
# soma(4) dá erro pq precisa receber 2 valores
# soma(9, 9, 5) dá erro pq ele só consegue identificar dois valores
mude()
def contador(*num):# O * serve para dizer que eu não sei quantas info o cara vai mandar então se prepara.(DESEMPACOTAMENTO)
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
mude()
valores = [6, 3, 9, 1, 0, 2]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)