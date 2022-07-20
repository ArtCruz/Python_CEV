p = float(input('Qual o preço do produto? '))
print('O preço com \033[0;31m5%\033[m de desconto será de \033[0;34m{:.2f} reais\033[m. '.format(p*0.95))
