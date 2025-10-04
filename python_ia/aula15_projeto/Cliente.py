class Cliente:

    def __init__(self,nome,telefone,email,cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def email(self):
        return self.__email
    
    @property
    def cpf(self):
        return self.__cpf
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def nome(self, telefone):
        self.__telefone = telefone
    
    @email.setter
    def email(self, email):
        self.__email = email

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf