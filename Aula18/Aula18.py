teste = list()
teste.append('Arthur')
teste.append('18')
galera = list()
galera.append(teste[:]) # Faz uma CÓPIA e não uma ligação
print(teste)
print('-=' * 20)
pessoal = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoal)
print(pessoal[0])
print(pessoal[2][1])
for p  in pessoal:
    print(f'{p[0]} tem {p[1]} anos')
print('-=' * 20)
people = list() 
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ').upper()))
    dado.append(int(input('Idade: ')))
    people.append(dado[:])
    dado.clear()
print(people)
for p in people:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} não é maior de idade')