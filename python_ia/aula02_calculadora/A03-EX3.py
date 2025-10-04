def notas(nota1,nota2, nota3):
    soma = nota1+nota2+nota3
    media = soma/3
    return media

nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))

print(f'A média do aluno é: {notas(nota1,nota2,nota3):.1f}')
