#
# Autores:
# Michel Silva
# Carlos Eduardo
#
# data: 27/06/2022
#
# 1.	Em linguagem Python, elabore um menu em loop.
#

# Menu com laço de repetição While

Menu = True # Variável de controle do loop do menu do programa (True = continua)

while Menu: # Loop While que continuará até opcao = False
  print("1 - Menu 1")
  print("2 - Menu 2")
  print("3 - Menu 3")
  print("4 - Menu 4")
  print("5 - Sair do loop")
  
  opcao = int(input("\nEntre a opção de [1-5]: ")) # Solicita a escolha do usuario e converte para inteiro (int)

  if opcao == 1: # Se opção recebida for igual a 1.
    print("\nMenu 1 foi selecionado\n") #"\n" é usado para quebrar uma linha, parecido com a tecla enter do teclado.
    # Você pode adicionar seu código ou funções aqui
  
  elif opcao == 2: # Se a opção recebida for igual a 2.
    print("\nMenu 2 foi selecionado\n")
    # Você pode adicionar seu código ou funções aqui
  
  elif opcao == 3: # Se a opção recebida for igual a 3.
    print("\nMenu 3 foi selecionado\n")
    # Você pode adicionar seu código ou funções aqui
  
  elif opcao == 4: # Se a opção recebida for igual a 4.
    print("\nMenu 4 foi selecionado\n")
    # Você pode adicionar seu código ou funções aqui
  
  elif opcao == 5: # Se a opção recebida for igual a 5.
    print("\nMenu 5 foi selecionado\n")
    # Você pode adicionar seu código ou funções aqui
    Menu = False  # Isso fará com que o loop while termine recebendo a váriavel menu como False.
  
  else: # Quaisquer entradas inteiras diferentes dos valores 1-5, imprimimos uma mensagem de erro
    print("\nSeleção de opção errada. Digite qualquer chave para tentar novamente ..\n")

print("fim do programa") # Informando para o usuário que o programa terminou
