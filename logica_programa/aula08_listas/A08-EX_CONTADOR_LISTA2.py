'''
Utilizando um for, imprima a soma das notas
Calcule a média das notas
'''
'''notas = [9.2,8.3,4.7]

soma = 0

for i in notas:
    soma += i

print(soma)
'''

notas = [9.2,8.3,4.7]

soma = 0
media = 0


for i in notas:
    soma = soma + i

media = soma / len(notas)

print(media)

'''
Também podemos utilizar o LEN para que ele retorne o tamanho da lista 
'''

soma = sum(notas)

"""
A função SUM retorna a soma de uma lista
"""

