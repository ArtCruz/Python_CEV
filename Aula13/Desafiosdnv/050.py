soma = 0
for n in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '.format(n)))
    if num % 2 == 0:
        soma += num
print('A soma dos numeros pares é {}'.format(soma))
