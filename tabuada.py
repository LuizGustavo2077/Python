valor = int(input("Digite qual tabua você que ver "))
var = str(input("Digite qual é a forma de. EX: *,+,/,- "))
if var == "+":
    for c in range(1,11):
        resu = valor+c
        print("{} + {} = {} ".format(valor,c,resu))
elif var == "-":
    for c in range(valor,valor+11,1):
        resu = c - valor
        print("{} - {} = {} ".format(c,valor,resu))
elif var == "*":
    for c in range(0,11):
        resu = valor*c
        print("{} * {} = {} ".format(valor,c,resu))
elif var == "/":
    for c in range(valor,valor*11,valor):
        resu = c/valor
        print("{} / {} = {} ".format(c,valor,resu))