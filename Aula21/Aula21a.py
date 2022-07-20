def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial() 
print(f'Os resultados são {f1}, {f2}, {f3}')
print('-=' * 30)
def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')