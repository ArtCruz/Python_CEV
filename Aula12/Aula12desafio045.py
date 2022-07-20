from random import choice
from time import sleep
print('Bora jogar um JOKEMPÔ!')
ped = "PEDRA", "PAPEL", "TESOURA"
comp = choice(ped)
esc = str(input('PEDRA, PAPEL ou TESOURA!!! ')).upper()
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ!')
print('-=' * 20)
if esc == comp:
    print('\033[4mEMPATE!Vamos de novo.\033[m')
    print('Você escolheu {} e eu escolhi {}.'.format(esc, comp))
elif esc == 'PAPEL' and comp == 'TESOURA' or esc == 'TESOURA' and comp == 'PEDRA' or esc == 'PEDRA' and comp == 'PAPEL':
    print('\033[31mDERROTA!Melhor chance na próxima vez.\033[m')
    print('Você escolheu {} e eu escolhi {}.'.format(esc, comp))
elif esc == 'TESOURA' and comp == 'PAPEL' or esc == 'PEDRA' and comp == 'TESOURA' or esc == 'PAPEL' and comp == 'PEDRA':
    print('\033[32mVITÓRIA!Parabéns por ter ganhado.\033[m')
    print('Você escolheu {} e eu escolhi {}.'.format(esc, comp))
else:
    print('Opçâo inválida. Tente novamente')
