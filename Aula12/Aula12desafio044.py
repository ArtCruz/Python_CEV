pr = float(input('Qual o valor do produto? R$'))
fp = int(input(('''Escolha uma das formas de pagamento:
[ 1 ] Dinheiro/Cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
A forma de pagamento será: ''')))
if fp == 1:
    print('Se pagar pelo \033[4mdinheiro/cheque\033[m ao invés de pagar {:.2f}, você pagará {:.2f}.'.format(pr, pr * 0.9))
elif fp == 2:
    print('Se pagar \033[4mà vista no cartão\033[m ao invés de pagar {:.2f}, você pagará {:.2f}.'.format(pr, pr * 0.95))
elif fp == 3:
    print('Se pagar em 2x no cartão o preço continuará igual, ou seja {:.2f}.'.format(pr))
elif fp == 4:
    print('Se pagar em 3x ou mais no cartão ao invés de pagar {:.2f}, você pagará {:.2f}.'.format(pr, pr * 1.2))
else:
    print('\033[31mOpção inválida, tente novamente.\033[m')
