name = []
scores = []
x = []
w = []
media = []

while True:
    nome = str(input('Nome: ')).capitalize()
    scores.append(nome)
    n1 = float(input('Nota 1: '))
    name.append(n1)
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    media.append(m)
    name.append(n2)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    x.append(scores[:])
    x.append(name[:])
    w.append(x[:])
    scores.clear()
    name.clear()
    x.clear()
    if continuar == 'N':
        print('-=' * 15)
        print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
        print('--' * 15)
        for i, a in enumerate(w):
            print(f'{i}  {w[i][0]}       {media[i]:.1f}')
        print('--' * 15)
        while True:
            aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            for i, a in enumerate(w):
                if aluno == i:
                    print(f'Notas de {w[i][0]} são {w[i][1]}')
                    print('-=' * 22)
            if aluno == 999:
                print('Volte Sempre!')
                break
        break
print(w)