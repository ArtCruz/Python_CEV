import math
an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
print('O ângulo de \033[4;35m{}\033[m possui \033[4mseno\033[m de \033[7;33m{:.2f}.\033[m'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de \033[4;35m{}\033[m possui um \033[4mcosseno\033[m de \033[7;33m{:.2f}.\033[m'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de \033[4;35m{}\033[m possui uma \033[4mtangente\033[m de \033[7;33m{:.2f}.\033[m'.format(an, tangente))