'''
CRIE UM MENU COM AS SEGUINTES OPÇÕES:
1- CADASTRAR ALUNO
SOLICITE O NOME AO USUÁRIO E ADICIONE AO FINAL DA LISTA
2- IMPRIMIR LISTA DE ALUNOS
3- SAIR
'''

nomes = []

while True:
    print('-----------MENU-----------')
    print('1- CADASTRO DE ALUNO')
    print('2- LISTA DE ALUNOS')
    print('3- SAIR.')
    opcao = int(input('Selecione uma opção:'))

    if opcao == 1:
        nome = input('Informe seu nome:')
        nomes.append(nome)

    elif opcao == 2:
        for i in nomes:
            print(i)
    
    elif opcao == 3:
        print('Você está saindo.')
        break

    else:
        print('Opção Inválida, tente novamente!')



