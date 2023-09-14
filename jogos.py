
import forca
import adivinhação

print("*********************************")
print("**********Escolha o seu jogo!**********")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual o jogo?"))

if(jogo ==1):
    print("jogando Forca")
    import forca
    forca.jogar()
elif(jogo ==2):
    print("Jogando advinhação")
    import adivinhação 
    adivinhação.jogar()

print("Fim do jogo")
