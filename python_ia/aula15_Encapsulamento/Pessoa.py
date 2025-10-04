class Pessoa:
    def __init__(self,nome):
        self.__nome = nome  #Usamos 2 underline para identificar um atributo privado
    
    def setNome(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome


pessoa1 = Pessoa("Rafael")

# pessoa1.__nome= "Murilo" 
 
#ESSA FORMA TBM É POSSÍVEL MAS N ESTÁ DENTRO DAS CONVENÇÕES

#print(pessoa1.__nome) 


pessoa1.setNome("Murilo")

print(pessoa1.getNome())