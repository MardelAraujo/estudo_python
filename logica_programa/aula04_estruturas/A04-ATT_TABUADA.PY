numero = int(input("Informe um numero para gerar a tabuada:"))
aux = 1
resultado = 0
while aux <= 10:
  resultado = numero * aux
  print(f"{numero} x {aux} = {resultado}")
  aux +=1

print("Fim!")