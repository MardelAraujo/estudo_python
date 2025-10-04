from terreno import *

valor1_digitado = float(input('Informe o primeiro valor :'))

valor2_digitado = float(input('Informe o segundo valor:'))

resultado = calcular_area_terreno(valor1_digitado,valor2_digitado)

print(f'A area do terreno é de {resultado} m2')