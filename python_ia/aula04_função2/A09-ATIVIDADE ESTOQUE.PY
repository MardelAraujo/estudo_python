from functools import reduce
'''
Considere que a seguinte lista representa os
valores de produtos de um estoque
1 - Realize um filtro para buscar todos os itens no estoque que possuem
valor maior que 60

2 - Nos itens já filtrados no item anterior, 
execute uma operação para realizr um desconto de 20 % nos valores de cada item da lista
filtrada

3 - Execute a soma dos itens da lista anterior usando o reduce.
'''

lista_estoque = [80.30, 90.2, 87,40, 23.30, 50.10, 60.30]

lista_filtro = list(filter(lambda x:x>60,lista_estoque))

lista_desconto = list(map(lambda x: x*0.8,lista_filtro))

list_red = reduce(lambda x,y: x+y,lista_desconto)

print(list_red)