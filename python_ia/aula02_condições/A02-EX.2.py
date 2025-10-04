lista_alunos = [
    {"nome":"Fabiano Sarpa","curso":"DEV", "notas":[8.0, 7.2, 9.3]},
    {"nome":"Juliano Mascarenhas","curso":"DEV","notas":[8.0, 5.3, 4.3]},
    {"nome":"Fernando Rabaçal","curso":"Design","notas":[8.0, 5.3, 4.3]},
    {"nome":"Ilario Fernanes","curso":"Design","notas":[7.0, 5.3, 4.3]},
    {"nome":"Liliana Macedo","curso":"DEV","notas":[8.0, 9.2, 5.3]},
    ]

#Imprima a soma da notas dos alunos do curso DEV

for curso in lista_alunos:
    if curso['curso'] == 'DEV':
        soma = sum(curso['notas'])
        media = soma /len(curso['notas'])
        print(f' Aluno: {curso['nome']}, Média: {media:.2f}')
              
      
              
