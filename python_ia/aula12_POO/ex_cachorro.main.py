from classe_cachorro import Cachorro

lista = []

print('------------- PREENCHA AS INFORMAÇÕES DO PET -------------')

nome_1 = input('Informe o nome do cachorro:')

raca_1 = input('Informe a raça do cachorro:')

idade_1 = int(input('Informe a idade do cachorro:'))

cachorro_1 = Cachorro(nome_1, raca_1, idade_1)

lista.append(cachorro_1)

print(lista[0].nome)

#print(f'Nome:{cachorro_1.nome} \nRaça:{cachorro_1.raca}\nIdade:{cachorro_1.idade}')

