import random
import math
resultado = math.ceil(random.random() *10)

while True:
    num_informado = int(input('Informe um numero inteiro entre 0 e 10:'))

    if num_informado == resultado:
        print('O tigrinho soltou a carta!')
        break

    else:
        print('Não foi dessa vez, tente denovo!')


    