class Pessoa:
    def __init__(self,nome):
        self.__nome = nome

    @property

#FUNCIONA COMO O GET

    def nome(self):
        return self.__nome
    
    @nome.setter

#FUNCIONA COMO O SET

    def nome(self, nome):
        self.__nome = nome

    
pessoa1 = Pessoa("Rafael")

pessoa1.nome = "João"

print(pessoa1.nome)