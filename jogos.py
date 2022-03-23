import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("******  (1)   Forca        ******")
    print("******  (2)   Adivinhação  ******")
    print("*********************************")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        print("")
        print("")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando adivinhação")
        print("")
        print("")
        adivinhacao.jogar()

    else:
        print("Você não escolheu uma opção válida")
        escolhe_jogo()

if(__name__ == "__main__"):
    escolhe_jogo()
