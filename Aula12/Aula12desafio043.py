peso = float(input('Qual o seu peso em kg? '))
alt = float(input('Qual a sua altura em metros? '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f} mostrando que você está \033[4mabaixo do peso.\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f} mostrando que você está com um \033[4mpeso ideal.\033[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f} mostrando que você está com \033[4msobrepeso.\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f} mostrando que você está \033[4mobeso.\033[m'.format(imc))
else:
    print('Seu IMC é de {:.1f} mostrando que você está com \033[4mobesiade morbida.\033[m'.format(imc))
