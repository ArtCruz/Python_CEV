num = int(input('Quantos números na sequencia de Fibonacci você quer ver? '))
contador = 0
x = 0
y = 1
while contador < num - 2:
    if contador == 0:
        print('0 -> 1 -> ', end='')
    z = x + y
    print(z, end=' -> ')
    x = y
    y = z
    contador += 1
    if contador == num - 2:
        print('FIM', end='')