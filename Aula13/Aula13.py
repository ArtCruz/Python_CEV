for c in range(1, 4):  #Ele vai de um até o 3,99999 mas não conta o 4.
    print('OI')
print('FIM')
print('-=' * 20)
for c in range(0, 6):
    print(c)
print('-=' * 20)
for c in range(6, 0, -1):
    print(c)
print('-=' * 20)
for c in range(0, 7, 2):
    print(c)
print('-=' * 20)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo:'))
for c in range(i, f+1, p):
    print(c)
print("-=" * 20)
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')
print('-=' * 20)
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores foi {}.'.format(s))
