'''CRIE UM MENU COM 2 OPÇÕES
1- IMPRIMIR A TABUADA DO NUMERO SOLICITADO
2- SAIR'''

while True:
    print("Menu:")
    print("1- Escolhar um numero para ver a tabuada")
    print('2-Sair')
    nmenu = int(input('Escolha uma opção:'))

    if nmenu == 1:
        num = int(input("Escolha um número:"))

        for i in range(1,11):
            print(f'{num}x{i} = {num*i}')

    elif nmenu == 2:
        print("Você saiu do programa.")
        break

    else:
        print("Digite uma opção válida.")