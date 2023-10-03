#ax² + bx + c
def bhaskara(a,b,c):
    delta = (b**2) -(4*a*c)
    if delta <0:
        print ("Sem soluçãom não tem real")
    else:
        x1= (-b + (delta **(1/2)))/ (2*a)
        x2= (-b - (delta **(1/2)))/ (2*a)
        print("X1 = {}| X2 = {}".format(x1,x2))
#testando os valores
bhaskara(1,12,-13)

valorA= int(input("Digite p valor A"))
valorB= int(input("Digite p valor B"))
valorC= int(input("Digite p valor C"))
bhaskara(valorA,valorB,valorC)