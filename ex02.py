
#
# autores:
# Michel Silva
#
# data: 26/06/2022
#
# 2.	Em linguagem Python, faça um programa que sorteia um valor entre 1 e 10 e solicite ao usuário
# que adivinhe esse número sorteado.
#
# import random
from random import randint # importa a função randint do módulo random

numero_sorteado = randint(1, 10) # sorteia um número entre 1 e 10 e atribui a variável numero_sorteado
contador = 3 # contador de tentativas do usuário

while contador > 0: # loop while que continuará até contador = 0
    chute = int(input("Digite um número entre 1 e 10: ")) # recebe o chute do usuário e converte para inteiro (int)
    if chute == numero_sorteado: # se o chute do usuário for igual ao número sorteado (numero_sorteado)
        print("Você acertou!") # imprime mensagem de acerto ao usuário
        break # sai do loop while (break)
    else: # se o chute do usuário não for igual ao número sorteado (numero_sorteado)
        print("Você errou!") # imprime mensagem de erro ao usuário
        contador -= 1 # decrementa o contador de tentativas do usuário
        if contador == 0: # se o contador de tentativas do usuário for igual a 0
            print("Você perdeu!") # imprime mensagem de perda ao usuário
            break # sai do loop while (break)
        else: # se o contador de tentativas do usuário não for igual a 0
            print(f"Você ainda tem {contador} tentativas") # imprime mensagem de quantas tentativas o usuário ainda tem

print("Fim do programa")
