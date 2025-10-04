class Armazem:
    def __init__(self,nome,telefone, listaCafes):
        self.nome = nome
        self.telefone = telefone
        self.listaCafes = listaCafes
        

class Cafe:
    def __init__(self,tipo,armazem):
        self.tipo = tipo
        self.armazem = armazem
        

armazem1 = Armazem("Presidente Vargas","997654123",[])
cafe1 = Cafe("Connilon",armazem1)
cafe2 = Cafe("Arábica",armazem1)

armazem1.listaCafes.append(cafe1)
armazem1.listaCafes.append(cafe2)

for cafe in armazem1.listaCafes:
    print(cafe.tipo)