#
# Autores:
# 
# Michel Silva
# Carlos Eduardo
# 
# data: 27/06/2022
#
# 2.	Em linguagem Python, faça um programa que sorteia um valor entre 1 e 10 e solicite ao usuário
# que adivinhe esse número sorteado.
#

# Importando a função randint() da biblioteca ou módulo random.
from random import randint

numero_sorteado = randint(1, 10) # Sorteia um número entre 1 e 10 e atribui a variável numero_sorteado
contador = 3 # Contador de tentativas do usuário

while contador > 0: # loop while que continuará enquanto a váriavel contador for maior que 0.

    chute = int(input("Digite um número entre 1 e 10: ")) # Recebe o chute do usuário e converte para inteiro (int)
    
    if chute == numero_sorteado: # Se o chute do usuário for igual ao número sorteado
        print("\nVocê acertou, parabéns que sorte!!!") # Imprime mensagem de acerto ao usuário
        break # Sai do loop while (break)
    
    elif chute > 10 or chute < 0: # Se o usuário informar um valor maior que 10 ou menor que 0 executa a identação.
        print('\nEii, lembre da regra, apenas valores inteiros entre 1 e 10.\n') # Imprimindo mensagem de erro
        continue # Continue volta pra primeira linha de código do while (continue).

    else: # Se o chute do usuário não for igual ao número sorteado (numero_sorteado)
        print("\nVocê errou!") # Imprime mensagem de erro ao usuário
        contador -= 1 # Decrementa o contador de tentativas do usuário
        
        if contador == 0: # Se o contador de tentativas do usuário for igual a 0
            print("\nQue pena, você acabou perdendo!") # Imprime mensagem de perda ao usuário
            print(f"O número sorteado era o: {numero_sorteado}") # Revela qual era o número escondido
        
        else: # se o contador de tentativas do usuário não for igual a 0
            print(f"\nNão desanime, você ainda tem {contador} tentativas\n") # Imprime mensagem de quantas tentativas o usuário ainda tem

print("\nfim do programa") # Informa ao usuário que o programa chegou ao fim
