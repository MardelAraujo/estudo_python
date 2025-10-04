class Autor:

    def __init__(self,nome):
        self.nome = nome

class Livro:

       def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


autor1 = Autor("João Silva")
livro1 = Livro("Aventuras na floresta",autor1)

print(livro1.autor.nome)

        

