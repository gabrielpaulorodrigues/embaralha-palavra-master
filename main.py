import random
from listas import *


def linha():
    print(20 * '=')


def menu():
    linha()
    print('Embaralha Palavra')
    linha()


def dificuldade():

    print('Escolha a dificuldade:')
    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')
    linha()

    global escolha_dificuldade

    escolha_dificuldade = int(input('Escolha: '))

    if escolha_dificuldade > 3 or escolha_dificuldade < 1:
        print('Dificuldade inválida! Tente novamente.')
        dificuldade()

    return escolha_dificuldade


def tema():

    linha()
    print('Escolha o tema:')
    print('1 - Animais')
    print('2 - Países')
    print('3 - Cidades')
    linha()

    global escolha_tema

    escolha_tema = int(input('Escolha: '))

    if escolha_tema > 3 or escolha_tema < 1:
        print('Tema inválido! Tente novamente.')
        tema()


def sorteio():  # sorteia a palavra

    if escolha_tema == 1:
        palavra = animais[escolha_dificuldade-1]
    elif escolha_tema == 2:
        palavra = paises[escolha_dificuldade-1]
    elif escolha_tema == 3:
        palavra = cidades[escolha_dificuldade-1]

    global palavra_sorteada

    palavra_sorteada = random.choice(palavra)

    return palavra_sorteada


def embaralha():

    global palavra_formatada

    palavra_embaralhada = list(palavra_sorteada)

    random.shuffle(palavra_embaralhada)

    palavra_formatada = "".join(palavra_embaralhada)

    return palavra_formatada


def acertos():

    frases_motivacao = ["Tente novamente, não desista!!.",
                        "Vamos lá você consegue!", "Tente novamente está quase lá", "Nunca desista"]

    chute = 0
    tentativas = 5

    escolha_frase_motivação = random.choice(frases_motivacao)

    print(f"Você tem {tentativas} tentativas para acertar a palavra.")
    print(f"A palavra embaralhada é: {palavra_formatada}")

    while True:
        jogador = input("\nDigite a palavra: ")

        if jogador == palavra_sorteada:
            print(
                f"Parabens você acertou na {chute+1}° tentativa")
            break

        elif chute <= 3:
            print(escolha_frase_motivação)
            chute += 1

        print(f"{tentativas-1} tentativas restantes")
        tentativas -= 1

        if tentativas == 0:
            print(f"Nāo foi dessa vez, a palavra era{palavra_sorteada}")
            break


menu()
dificuldade()
tema()
sorteio()
embaralha()
acertos()
