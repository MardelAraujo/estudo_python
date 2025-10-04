"""
CRIE UMA CLASSE CARRO QUE TERA APENAS 1 ATRIBUTO PRIVADO CHAMADO VELOCIDADE
CONTRUA O METODO CONSTRUTOR E OD METODOS GET E SET PARA O ATRIBUTO
CRIE UM OBJETO DO TIPO Carro
ATRIBUA UMA VELOCIDADE PARA ELE USANDO O SET
IMPRIMA O VALOR USANDO O GET

"""


class Carro:

    def __init__(self,velocidade):
        self.__velocidade = velocidade


    def setVelocidade(self,velocidade):
        if(velocidade>=0):

            self.__velocidade = velocidade
        else:
            print("Velocidade não pode ser negativa!")


    def getVelocidade(self):
        return self.__velocidade
    

vcarro1 = Carro(10)

vcarro1.setVelocidade(-2)

print(vcarro1.getVelocidade())