'''
Calculem e imprimam a média  dos alunos da lista abaixo
'''

alunos = [{
    "nome":"Fernando Rebouças",
    "curso":"Dev full stack",
    "idade":28,
    "matriculado":True,
    "notas":[8.0, 7.2, 6.5]
    },{
    "nome":"Juliano Oliveira",
    "curso":"Dev full stack",
    "idade":31,
    "matriculado":True,
    "notas":[5.4, 7.2, 6.3]
    },{
    "nome":"Kiliana Olivença",
    "curso":"Dev full stack",
    "idade":22,
    "matriculado":True,
    "notas":[6.1, 7.2, 8.3]
    }]


for aluno in alunos:
    soma = sum(aluno['notas'])
    media = soma /len(aluno['notas'])
    print(f'A media de {aluno['nome']} é {media:2f}')
    
    
    