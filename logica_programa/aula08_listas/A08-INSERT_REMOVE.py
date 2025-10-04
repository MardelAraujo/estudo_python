notas = [8, 9, 10]

notas.insert(0,7)

'''
Utilizando o Insert podemos escolher em primeiro lugar a posição em que o elemento vai ser adicionado e, separado por virgula, o elemento que será adicionado
Nesse caso a lista vai se tornar [7,8,9,10] pois adicionei na posição 0 o elemento 7

'''

print(notas)

notas.remove(7)

'''
Pode ser utilizado para remover o primeiro item que encontrar com o valor indicado
Nesse caso ele removerá o primeiro numero 7 que encontrar do primeiro até o ultimo
'''

print(notas)

notas.pop(0)

'''
Já o Pop remove o item pela posição indicada, ou, caso não seja indicada uma posição, vai ser remover o ultimo
Nesse caso ele vai remover o numero 8 pois está na posição 0
'''