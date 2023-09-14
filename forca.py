import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["-" for letra in palavra_secreta]


    enforcou = False
    acertou = False

    erros = 0
    tentativas_restantes = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        
        if(chute.upper() in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            tentativas_restantes -= 1
            print("você errou, não existe a letra {}: ".format(chute))
            print("Você errou {} vez e ainda tem {} tentativas".format(erros, tentativas_restantes))

        if(erros == 6):
            print("Você perdeu ")
            break

        if "-" not in letras_acertadas:
            acertou = True    
            

            

        print(letras_acertadas)
    if acertou:
        print("Parabéns! Você acertou a palavra secreta: {}".format(palavra_secreta))
    else:
        print("Fim do jogo. A palavra secreta era: {}".format(palavra_secreta))
    

if(__name__ == "__main__"):
    jogar()
