from functools import reduce


lista_estoque = [80.30, 90.2, 87,40, 23.30, 50.10, 60.30]

lista_filtro = list(filter(lambda x:x>60,lista_estoque))

lista_desconto = list(map(lambda x: x*0.8,lista_filtro))

list_red = reduce(lambda x,y: x+y,lista_desconto)

print(list_red)

'''
python -m venv myenv

No Windows: myenv/scripts/activate

No macOS e Linux: source myenv/bin/activate
'''