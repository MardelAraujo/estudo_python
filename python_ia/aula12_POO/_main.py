from classe_carro import Carro

carro_1 = Carro("March", "Prata", 2014)
carro_2 = Carro('Uno', 'Verde', 1992)


print(carro_1.cor)

print(carro_2.ano)

carro_1.acelerar()

print(carro_1.velocidade)

carro_1.frear(11)

print(carro_1.velocidade)



