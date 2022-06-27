#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 1.	Em linguagem Python, elabore um menu em loop.
#
#

# menu
opcao = True # variavel de controle do loop do menu do programa (True = continua)

while opcao:  ## Loop While que continuará até opcao = False
  print("1- opção 1")
  print("2- opção 2")
  print("3- opção 3")
  print("4- opção 4")
  print("5- opção sair")
  menu = int(input("entre a opção de [1-5]: ")) # recebe a opção do menu do usuario e converte para inteiro (int)

  if menu == 1: # opção 1 do menu (1)
    print("Menu 1 foi selecionado")
    ## Você pode adicionar seu código ou funções aqui
  elif menu == 2: # opção 2 do menu (2)
    print("Menu 2 foi selecionado")
    ## Você pode adicionar seu código ou funções aqui
  elif menu == 3: # opção 3 do menu (3)
    print("Menu 3 foi selecionado")
    ## YVocê pode adicionar seu código ou funções aqui
  elif menu == 4: # opção 4 do menu (4)
    print("Menu 4 foi selecionado")
    ## Você pode adicionar seu código ou funções aqui
  elif menu == 5: # opção 5 do menu (5)
    print("Menu 5 foi selecionado")
    ## Você pode adicionar seu código ou funções aqui
    opcao = False  # Isso fará com que o loop while termine, já que o valor do loop não é definido como False
  else:
    # Quaisquer entradas inteiras diferentes dos valores 1-5, imprimimos uma mensagem de erro
    print("Seleção de opção errada. Digite qualquer chave para tentar novamente ..")

print("Fim do programa")