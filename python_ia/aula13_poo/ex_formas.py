import math

class Formas:

    def __init__(self,nome):
        self.nome = nome
        
    
    def calcularPerimetro(self):
        pass
    
    def calcularArea(self):
        pass
              

class Retangulo(Formas):

    def __init__(self, base, altura,nome):
        super().__init__(nome)
        self.base = base
        self.altura = altura
    
    def calculaPerimetro(self):
        return 2*(self.base + self.altura)
    
    def calculaArea(self):
        return self.base*self.altura


    
class Circulo(Formas):

    def __init__(self,raio):
        self.raio = raio

    def calcularPerimetro(self):
        return 2* math.pi * self.raio
    
    def calcularArea(self):
        return math.pi * (self.raio**2)
    

retangulo1 = Retangulo(3,5)

print(retangulo1.calculaArea())
print(retangulo1.calculaPerimetro)
