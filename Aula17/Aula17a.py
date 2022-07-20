num = [2, 5, 9, 1]
num[2] = 3 # Na posição 2 troque o 9 pelo 3 
num.append(7) # Adicione o valor 7(irá criar uma nova "casa" no final da lista e ficará lá)
print(num.sort(reverse=True)) # O sort é usado para organizar na ordem crescente e o reverse=True reverte logo fica na ordem decrescente
num.insert(2, 2) # Na posição 2 adicione o 2 e bote o resto prolado
num.pop() # remove o ultimo elemento da lista
 # num.pop(2) removeria o segundo elemento da lista
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Eu não achei o número 4 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')