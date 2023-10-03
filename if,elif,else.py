# determinando se o aluno com basa na nota
nota = int(input\
("Qual foi a nota do aluno (Digite um valor entre 0 de 10)"))
if nota == 10:
    print  ("aprovado.Excelente trabalho")
elif nota >=7 and nota <= 9:
    print ("aprovado.Bom trabalho")
elif nota == 6:
    print ("Aprovado( não fez mais que o obrigação)")
elif nota <=5:
    print ("repetiu de ano")
else:
    print ("valor não identificado")