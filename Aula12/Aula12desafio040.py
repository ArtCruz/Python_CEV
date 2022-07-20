n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
media = (n1 + n2) / 2
print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}.'.format(n1, n2, media))
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
