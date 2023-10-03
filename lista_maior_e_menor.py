# [4, 5, 7, 20, 2, 4, 5]
def maior_valor(lista):
    maior = 0
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

# [4, 5, 7, 20, 2, 4, 5]
def menor_valor(lista):
    menor = 100
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor
resultado1= maior_valor([4, 5, 7, 20, 2, 4, 5])
resultado2= menor_valor([4, 5, 7, 20, 2, 4, 5])
print(resultado1)
print(resultado2)
def quantidade_lista(lista):
    qnt =0
    for x in lista:
        qnt +=1
    return qnt
resultado3= quantidade_lista([4, 5, 7, 20, 2, 4, 5])
print(resultado3)