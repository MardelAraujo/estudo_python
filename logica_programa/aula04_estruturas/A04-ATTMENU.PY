'''Crie um menu com 3 opções
1 - Soma
2 - Subtração
3 - Sair
Se o usuário digitar 1, solicite 2 numeros e realize a soma
Se o usuário digitar 2, solicite 2 numeros e realize a subtração
Se o usuário digitar 3, saia do programa
'''

opcao = ""

while opcao != "3":
  print("Menu")
  print("1 - SOMA")
  print("2 - SUBTRAÇÃO")
  print("3 - Sair")
  opcao = input("Digite uma opção:")

  if opcao == "1":

    num1 = int(input("Digite o primeiro número para soma:"))
    num2 = int(input("Digite o segundo número para soma:"))
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

  elif opcao == "2":
    sub1 = int(input("Digite o primeiro número para subtração:"))
    sub2 = int(input("Digite o segundo número para subtração:"))
    resul2 = sub1 - sub2
    print(f"Resultado: {resul2}")

  elif opcao == "3":
    print("Você Saindo...")

  else:
    print("Opção Invalida!")
  