class Carro:
    #CONVENÇÃO DE BOA PRÁTICA: INICIAR A CLASSE COM LETRA MAIUSCULA

    def __init__(self, modelo, cor, ano):

        #A FUNÇÃO RESPONSÁVEL POR PEGAR OS ATRIBUTOS DE UMA CLASSE É CHAMADA DE MÉTODO CONSTRUTOR PRESENTADOR POR __inin__ (2 underline)

        #OS PARÂMETROS SÃO AS VARIÁVEIS QUE VAMOS COLETAR

        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0

        #AS CARACTERISTICAS DE UMA CLASSE, NESSE CASO, AS CARACTERISTICAS QUE VÃO DEFINIR O CARRO SÃO CHAMADOS DE ATRIBUTOS
    
    def acelerar (self):
        #AS CLASSES TAMBÉM PODEM TER MÉTODOS QUE PODE DEFINIR DE QUE FORMA UM ATRIBUTO PODE AGIR

        self.velocidade = self.velocidade + 10

    def frear (self, velocidade):

        #PODEMOS PASSAR UM MÉTODO PARA O MÉTODO SONTRUTOR, DESSA FORMA, QUANDO A FUNÇÃO FREAR FOR CHAMADA, É NECESSÁRIO PASSAR O MÉTODO
        #carro_1.frear(-5)
        if (self.velocidade - velocidade < 0):

            print('A velocidade não pode ser inferior à 0')
        else:
            
              self.velocidade -= velocidade
