class Biblioteca:

    def __init__(self,nome):
        self.nome = nome
        self.livros = []

class Livro:
    def __init__(self,titulo, biblioteca = None):
        self.titulo = titulo
        self.biblioteca = biblioteca


biblioteca1 = Biblioteca("Central")
livro1 = Livro("Aventuras na floresta")
livro1.biblioteca = biblioteca1
biblioteca1.livros.append(livro1)