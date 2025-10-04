
aluno = {
    "nome" : "Fernando Rebouças",
    "curso" : "DEV Full Stack",
    "idade" : "28",
    "matriculado" : True,
    "Notas": [8.0,7.2,6.5]
}

soma = sum(aluno["Notas"])
media = soma / len(aluno["Notas"])
print(f'A media do aluno {aluno["nome"]} é {media:.2f}')