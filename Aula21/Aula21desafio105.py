def notas (*n, sit=False):
    """
    NOTAS DA TURMA
    param n: uma ou mais notas dos alunas (aceita várias)
    param sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informaçôes sobra a turma
    """
    r = dict()
    r['TotalProvas'] = len(n)
    r['MaiorNota'] = max(n)
    r['MenorNota'] = min(n)
    r['MédiaTurma'] = sum(n)/len(n)
    if sit:
        if r['MédiaTurma'] >= 7:
            r['Situação'] = 'BOA'
        elif r ['MédiaTurma'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r
resp = notas(5.5, 2.5, 9, 8.5, sit= True)
print(resp)
help(notas)