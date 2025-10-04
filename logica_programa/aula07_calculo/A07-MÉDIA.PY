'''CRIE UM ALGORITIMO QUE PEÇA 4 NOTAS PARA O USUARIO
CALCULE A MÉDIA E DIGA SE O ALUNO FOI APROVADO OU NÃO'''

nota_1 = float(input("Informe a primeira nota:"))

nota_2 = float(input("Informe a segunda nota:"))

nota_3 = float(input("Informe a terceira nota:"))

nota_4 = float(input("Informe a quarta nota:"))


media = (nota_1 + nota_2 + nota_3 + nota_4)/4

if media >= 6:
    print(f"Sua média foi:{media}")
    print("Aluno Aprovado!")

if media < 6:
    print(f"Sua média foi:{media}")
    print("Aluno Reprovado!")