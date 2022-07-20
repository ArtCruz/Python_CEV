tupla = ('associação', 'boneca', 'caneca', 'domingo', 'escola', 'faculadade', 'gaiola', 'helicóptero', 'igreja',
         'joinville', 'kiwi', 'lagoa', 'macaco', 'Navio', 'oculos', 'Pato', 'Queijo', 'Rato', 'Sabado', 'Tatu', 'urubu',
         'Vacina', 'Well', 'Xixi', 'Yellow', 'Zebra')
for p in tupla:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
