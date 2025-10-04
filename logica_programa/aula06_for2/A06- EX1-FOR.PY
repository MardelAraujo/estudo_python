while True:
    numero1= int(input('Informe o inicio:'))
    numero2= int(input('Informe o fim:'))

    if numero1 > numero2:
        print('Formato inválido, digite um inicio menor que o fim.')
    else:
        break

for i in range(numero1,numero2+1):
    if i % 2 == 0:
        print(i)