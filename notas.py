#lista de alunos
notas_de_alunos = {
    "Garbriel": 8,
    "Luiz": 10,
    "Vitor": 3,
    "Elias": 7,
    "Murilo" :2,
    "Emily": 6
}
#Variavel aluno recebe os nomes dentro de notas
for aluno in notas_de_alunos:
    notas= notas_de_alunos[aluno]
#testas todos os alunos com as notas 
    if notas >=8:
        print("{} passou com {}, parabéns".format(aluno,notas))
    elif notas >=6:
         print("{} passou com {}, por pouco".format(aluno,notas))
    elif notas < 6:
        print("{} não passou com {}, seu burro".format(aluno,notas))