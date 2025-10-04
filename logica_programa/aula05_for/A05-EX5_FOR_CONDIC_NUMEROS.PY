'''ESCREVA UM PROGRAMA QUE SOLICITE 1 NUMERO POSITIVO AO USUARIO 
CONTE QUANTOS NUMEROS PARES E IMPARES EXISTEM DE 0 ATÉ O NUMERO ESCOLHIDO'''

numero = int(input("Informe um numero:"))
pares = 0
impares = 0

for i in range(1,numero+1):
  if i % 2 == 0:
    pares += 1
  else:
    impares += 1

print(f"Existem {pares} numeros pares e {impares} numeros impares.")