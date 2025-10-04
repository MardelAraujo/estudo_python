from calculadora import *

while True:
    print('--------CALCULADORA--------')
    print('1- SOMA')
    print('2- SUBTRAÇÃO')
    print('3- DIVISÃO')
    print('4- MULTIPLICAÇÃO')
    print('5- SAIR\n')
    opcao = int(input('- Digite uma opção:\n'))

    if opcao == 1:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {soma(num1,num2)}\n')

    if opcao == 2:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {sub(num1,num2)}\n')
    
    if opcao == 3:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {div(num1,num2)}\n')

    if opcao == 4:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {mult(num1,num2)}\n')

    if opcao == 5:
    
        print('Você está saindo do programa! Até a próxima.')
        break


