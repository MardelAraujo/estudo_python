'''
Solicite ao usuario sua idade
Se o usuario tiver mais de 31 anos
Imprima
"Você pode ser presidente"
Caso ele tenha entre 21 e 31 anos, imprima
"Você pode ser vereador"
Caso ele tenha menos de 21 anos:
"Você não pode ser candidato"
'''

nome = input('Infome seu Nome:')
idade = int(input('Informe sua Idade:'))

if idade > 31:
    print('Você pode ser Presidente')
elif idade >= 21 and idade <= 31:
    print('Você pode ser Vereador')
else :
    print('Você não pode ser candidato')