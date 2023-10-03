import csv
#lendo arquivo linha a linha
with open("./arquivo.txt","r") as arquivo:
    leitorCsv=csv.reader(arquivo,delimiter=";")
    numero_linha=0
    for valores in leitorCsv:
        if numero_linha>0:
            print("linha: {}".format(numero_linha))
            print("nome: {}".format(valores[0]))
            print("idade: {}".format(valores[1]))
            print("cidade: {}".format(valores[2]))
            print("casado: {}".format("Sim" if valores[3] =="TRUE" else "Não"))
            print("nome: {}".format(valores[4]))
            print("")
        
        numero_linha +=1