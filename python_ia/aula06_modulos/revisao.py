from functools import reduce

lista = [2,3,5,6,7,8]

lista_filtrada = list(filter(lambda x: x>=5,lista))
print(lista_filtrada)

lista_dobro = list(map(lambda x: x*2,lista_filtrada))
print(lista_dobro)

numero = reduce(lambda x,y: x+y,lista_dobro)
print(numero)