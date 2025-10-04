lista_alunos = [
    {"nome":"Fabiano Sarpa","nota":8.0},
    {"nome":"Juliano Mascarenhas","nota":9.2},
    {"nome":"Fernando Rabaçal","nota":6.3},
    {"nome":"Ilario Fernanes","nota":5.4}
    ]

#Imprima os alunos que tiraram nota abaixo de 7.0

for aluno in lista_alunos:
    if aluno["nota"]<7.0:
        print(aluno['nome'])