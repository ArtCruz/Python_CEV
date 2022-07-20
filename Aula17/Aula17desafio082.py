listapar = listaimpar = listageral = []
while True:
    n = int(input('Digite um número: '))
    listageral.append(n)
    if n %  2 == 0:
        listapar.append(n)
    elif n % 2 != 0:
        listaimpar.append(n) 
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
       break
listageral.sort()
listapar.sort()
listaimpar.sort()
print('-=' * 20)
print(f'A lista com todos os valores é {listageral}')
print(f'A lista com os valores \033[31mPARES é\033[m {listapar}')
print(f'A lista com os valores \033[32mIMPARES é\033[m {listaimpar}')