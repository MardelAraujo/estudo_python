'''
Crie 2 classes: 
  Escola:
    - nome
  Aluno:
    - nome
    - matricula
    - escola

No mesmo arquevo crie 2 escolas.
crie 4 alunos e associe 2 deles a cada escola
imprima o nome da escola de cada aluno  
'''

class Escola:
  def __init__(self,nome):
    self.nome = nome

class Aluno:
  def __init__(self, nome, matricula, escola):
    self.nome = nome
    self. matricula = matricula
    self.escola = escola

escola1 = Escola("Alzemira")
escola2 = Escola("Benezer")

aluno1 = Aluno("Leonardo Passos", 9583, escola1)
aluno2 = Aluno("Thiago Fernando", 9547, escola2)
aluno3 = Aluno("Marcus Vigas", 9572, escola2)
aluno4 = Aluno("Adriane Aragão", 9518, escola1)

print(f"O aluno1, {aluno1.nome} pertence a {aluno1.escola.nome}")
print(f"O aluno2, {aluno2.nome} pertence a {aluno2.escola.nome}")
print(f"O aluno3, {aluno3.nome} pertence a {aluno3.escola.nome}")
print(f"O aluno4, {aluno4.nome} pertence a {aluno4.escola.nome}")