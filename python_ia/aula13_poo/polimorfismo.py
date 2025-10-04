class Animal:
    def __init__(self, nome):
        
        self.nome = nome

    def fazerSom(self):
        print('hurg!')

    def fazerSom(self, dono):
        self.dono = dono
        print(f''hurg!', dono')

#POLIMORFISMO ESTÁTICO É QUNADO TEMOS DIVERSOS MÉTODOS DENTRO DE UMA MESMA CLASSE
#O QUE DEFINE QUAL METODO VAI SER CHAMADO VAI DEPENDER DOS PARÂMETRO PASSADO

class Cachorro(Animal):

    def fazerSom(self):
        print("Au!")

#JÁ O POLIMORFISMO DINÂMICO É QUANDO TEMOS DIVERSAS CLASSES COM O MESMO MÉTODO
#NESSE CASO, O QUE DEFINE O QUE VAI SER CHAMADO É A CLASSE