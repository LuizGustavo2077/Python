
def nome_da_sem_funcao():
    print("função sem argumento")
def nome_da_funcao(argumento1,argumento2):
    print("arg1:{} | arg2:{}".format(argumento1,argumento2))
def lista_de_argumento(lista):
    print(lista)
    for elemento in lista:
        print (elemento)
        
nome_da_sem_funcao()
nome_da_funcao("arg1", 5)
lista_de_argumento([1,2,3,4,5])