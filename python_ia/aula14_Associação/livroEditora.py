class Livro:
  def __init__(self, titulo, ano_publicação):
    self.titulo = titulo
    self.ano_publicação = ano_publicação

class Editora:
  def __init__(self,nome, email):
    self.nome = nome
    self.email = email

livro1 = Livro("Undertale", 2000)
print(livro1.titulo)
print(Editora.nome)