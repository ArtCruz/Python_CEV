#p1 = int(input('Numerador: '))
#p2 = int(input('Denominador: '))
#z = p1 / p2
#print(f'O resultado é {z}')

try: # Operação # Um "try" pode ter vários except
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # Falhou
    print(f'Problema encontrado foi {erro.__class__}')
else: # Deu Certo
    print(f'O resultado é {r}')
finally: #Certo/Falha
    print('Volte Sempre! Muito Obrigado')

try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else: # Deu Certo
    print(f'O resultado é {r}')
finally: #Certo/Falha
    print('Volte Sempre! Muito Obrigado')
