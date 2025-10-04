def calculo_area(altura,largura):
    return altura*largura

altura = float(input('Informe a altura do objeto:'))
largura = float(input('Informe a largura do objeto:'))

print(f'A área do objeto é:{calculo_area(altura,largura):.2f}')