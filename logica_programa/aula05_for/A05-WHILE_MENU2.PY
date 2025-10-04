'''Crie um menu com 3 opções
1. cadastro de pessoas
  1.1 Solicitar nome e idade
2. cadastro produtos
  2.1 Solicitar nome do produto e preço
3. Sair'''
opcao = None

while opcao != 3:
  print("Menu:")
  print("1- Cadastro de Pessoa:")
  print("2- Cadastro de Produto:")
  print("3- Sair")
  opcao = int(input("Escolha uma opção:"))

  if opcao == 1:
    nome=input("Infome seu nome:")
    idade=int(input("Infome sua idade:"))
    print(f"{nome} idade {idade}")
    print("Cadastro Concluido")

  elif opcao == 2:
    nomep=input("Infome o nome do produto:")
    valorp=float(input("Infome o valor do produto:"))
    print(f"{nomep} R${valorp}")
    print("Cadastro Concluido!")

  elif opcao == 3:
    print("Você está Saindo...")

  else:
    print("Opção Invalida, tente novamente.")


