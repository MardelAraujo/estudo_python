senha = int(input("Informe sua senha:"))
senha_u = 0

while senha != senha_u:
  senha_u = int(input("Informe a senha:"))
  if senha == senha_u:
    print("Senha Correta!")
  else:
    print("Senha Incorreta.")