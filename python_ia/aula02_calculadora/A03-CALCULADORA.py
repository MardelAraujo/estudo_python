def soma(num1,num2):
    return num1+num2
def subtração(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
def mult(num1,num2):
    return num1*num2

while True:
    print('--------CALCULADORA--------')
    print('1- SOMA')
    print('2- SUBTRAÇÃO')
    print('3- DIVISÃO')
    print('4- MULTIPLICAÇÃO')
    print('5- SAIR')
    opcao = int(input('- Digite uma opção: -'))

    if opcao == 1:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {soma(num1,num2)}')

    if opcao == 2:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {subtração(num1,num2)}')
    
    if opcao == 3:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {div(num1,num2)}')

    if opcao == 4:
        num1 = int(input('Informe o primeiro numero:'))
        num2 = int(input('Informe o segundo numero:'))
        print(f'A soma dos numeros é {mult(num1,num2)}')

    if opcao == 5:
    
        print('Você está saindo do programa! Até a próxima.')
        break

    

