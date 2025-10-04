peso = float(input("Informe seu peso em kg:"))

altura=float(input("Informe sua altura em metros:"))

imc = float(peso/(altura*altura))
'''OU imc = float(peso/(altura**2))'''

print(f"Seu indice de massa corporal é:{imc}")

if imc < 18.5:
  print("Você está abaixo do peso")
elif imc >= 18.5 and imc<=24.9:
  print("Vocẽ está Saudável")
elif imc >= 25 and imc <= 29.9:
  print("Você está com Sobrepeso")
elif imc > 29.9:
  print("Obesidade!")