senha = input("Informe sua senha:")

while True:
  print("Insira sua senha abaixo para sair")
  senha2 = input("Senha:")

  if senha2 == senha:
    print("Senha Correta!")
    break
  else:
    print("Senha incorreta, tente novamente.")
