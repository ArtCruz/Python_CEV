print('=-=' * 10)
print('Calculador de PA')
print('=-=' * 10)
num = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostra mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))