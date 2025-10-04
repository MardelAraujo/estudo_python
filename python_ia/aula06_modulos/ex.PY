def calcular_area_retangulo(base,altura):
    return base * altura

base_digitada = float(input('Informe o valor da base:'))

altura_digitada = float(input('Informe o valor da altura:'))

resultado = calcular_area_retangulo(base_digitada,altura_digitada)

print(resultado)