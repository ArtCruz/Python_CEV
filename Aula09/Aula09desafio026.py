f = str(input('Digite uma frase: ')).upper().strip()
print('A letra \033[7;34mA\033[m aparece \033[4;34m{} vezes.\033[m '.format(f.count('A')))
print('A letra \033[7;34mA\033[m apareceu na posição \033[4;34m{} pela primeira vez.\033[m ' .format(f.find('A')+1))
print('A letra \033[7;34mA\033[m apareceu na posição \033[4;34m{} pela última vez.\033[m '.format(f.rfind('A')+1))
x = 'prova em python'
print(len(x))
