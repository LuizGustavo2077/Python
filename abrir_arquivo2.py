with open("./arquivo.txt","r") as arquivo:
    numero_linha=1
    for linha in arquivo:
        print("{}:{}".format(numero_linha,linha))
        numero_linha +=1