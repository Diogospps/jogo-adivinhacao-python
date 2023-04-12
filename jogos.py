import forca
import adivinhacao

def escolher_jogo():

    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    print("(1) Jogo da Forca (2) Jogo da Adivinhacao")

    jogo = int (input("Escolha o jogo?\n"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhacao")
        adivinhacao.jogar()

if(__name__== "__main__"):
    escolher_jogo()