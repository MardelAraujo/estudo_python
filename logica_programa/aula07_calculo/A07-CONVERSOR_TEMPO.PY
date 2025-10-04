"""DESENVOLVA UM ALGORITIMO QUE CONVERTA UMA QUNATIDADE DE SEGUNDOS FORNECIDA PELO USUÁRIO EM HORAS, MINUTOS E SEGUNDOS"""

segundos_inf = int(input("Informe a quantidade de segundos:"))

horas = segundos_inf // 3600

'''O // PEGA O INTEIRO DA DIVISÃO'''

min = (segundos_inf % 3600) // 60

segundos = segundos_inf % 60

print(f'A quantidade de tempo é igual a {horas}:{min}:{segundos}')


