lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#  Tuplas são IMUTÁVEIS
#  Tuplas ()
#  Listas []
#  Dicionário {}
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[1:])
print(lanche[-3:])
print('---' * 15)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
print('---' * 15)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(len(lanche))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('---' * 15)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('---' * 15)
for pos, comida in enumerate(lanche):  # pos de posição
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))  # ORDEM alfabética
print('---' * 15)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(len(c))
print(c.index(8))
print(d)
print(d.count(2))
print(d.index(5, 1))  # Procure o 5 a partir da posição 1
print('---' * 15)
pessoa = ('Arthur', 18, 'M', 60)
# del(pessoa) apaga da memória
# del(pessoa[0]) a TUPLA não suporta apagar somente um termo pq é IMUTÁVEL
print(pessoa)
