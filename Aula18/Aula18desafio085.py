pares = []
impares = []
todos = []
for n in range(1, 8):
    num = int(input(f'Digite um  {n}º número: '))
    if num % 2 == 0:
        pares.append(num)
        
    else:
        impares.append(num)
(todos.append(pares))
todos[0].sort()
(todos.append(impares))
todos[1].sort()
print(f'Os valores PARES digitados foram: {todos[0]}')
print(f'Os valores ÍMPARES digitados foram: {todos[1]}')