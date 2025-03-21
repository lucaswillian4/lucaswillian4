alunos={}
materias =["portugues","matematica","historia","geografia","ingles"]
cont_aluno = 1
while (True):
    aluno=input(f"digite o nome do  º aluno")
    desempenho = []
    for i in range(1,5):
        print(f"{i}º BIMESTRE")
        notas=[]
        for n in range(0,5):
            nota=float(input(f"digite a nota do aluno em {materias[n]} ").replace(",",","))
            notas.appensd(notas)
        desempenho.append(notas)
    alunos[aluno] = desempenho

    opc=input("quer continuar? (s) ou (n)").lower()


    if(opc==input'n'):
        break
    cont_aluno+=1


# print(alunos)
# for a in alunos:
#     print(a)

medias = []
soma=[0,0,0,0,0]
boletim = {}
    for k