a = input('Digite algo: ')

print('\033[0;35mO tipo primitivo desse valor é {}.\n'
      '\033[0;32m Só tem espaços?\033[m {}.\n'
      '\033[0;31m Só tem números?\033[m {}.\n'
      ' \033[0;32mÉ alfabético?\033[m {}.\n'
      ' \033[0;31mÉ alfanumérico?\033[m {}.\n'
      ' \033[0;32mEstá em maiúsculo?\033[m {}.\n'
      ' \033[0;31mEstá minúsculo? {}.\033[m\n'    
      ' \033[0;32mEstá capitalizada?.\033[m {}\n'
      .format(type(a), a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle()))
