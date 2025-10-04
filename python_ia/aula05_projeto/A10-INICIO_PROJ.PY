lista_tarefa = []

while True:
    print('\n---------MENU---------\n')
    print('Opção 1- INCLUIR TAREFA')
    print('Opção 2- MOSTRAR TAREFAS')
    print('Opção 3- BUSCAR TAREFAS')
    print('Opção 4- EDITAR PRIORIDADE')
    print('Opçao 9- SAIR')

    resposta = int(input('Informe a opção:\n'))

    if resposta == 1:
        print('\n---------TAREFA---------\n')
        nome  = input('Infome o nome da tarefa:')
        descricao = input('Informe uma descrição:')
        prioridade = int(input('Defina uma prioridade de 1 a 5:'))
        while True:
            if (prioridade < 1 or prioridade >5):
                print('Valor inválido, tente novamente!')
            else:
                break

        categoria = input('Informe a categoria:')

        tarefa = dict()
        tarefa['nome'] = nome
        tarefa['descricao'] = descricao
        tarefa['prioridade'] = prioridade
        tarefa['categoria'] = categoria

        print(tarefa)

        lista_tarefa.append(tarefa)

    elif resposta == 2:
        print(lista_tarefa)
    
    elif resposta == 3:
        prioridade = int(input('Digite a prioridade a ser pesquisada:'))
        lista_prioridade = list(filter(lambda x:x['prioridade'] == prioridade, lista_tarefa))
        print(lista_prioridade)
        
    # RESPOSTA 3:
    # BUSCAR UM VALOR DENTRO DE UM DICIONÁRIO COM O FILTER

    elif resposta == 4:
        nome_pesquisa = input('Informe o nome da tarefa a ser pesquisada:')
        for indice in range(0,len(lista_tarefa)):
            print(lista_tarefa[indice])
            if nome_pesquisa == lista_tarefa[indice]['nome']:
                nova_prioridade = int(input('Digite a nova prioridade:'))
                lista_tarefa[indice]['prioridade'] = nova_prioridade
                print('Editado com sucesso!')
    # RESPOSTA 4:
    # COMANDO PARA ALTERAR UM VALOR DENTRO DE UM DICIONÁRIO DENTRO DA LISTA
    
    elif resposta == 9:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida, tente novamente.')

