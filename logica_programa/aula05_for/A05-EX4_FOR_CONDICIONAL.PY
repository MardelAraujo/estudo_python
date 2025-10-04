"""IMPRIMA SOMENTE AS VOGAIS DE UMA PALAVRA DIGITADA PELO USUÁRIO"""
palavra = input("Informe uma palavra:")

for i in palavra:
  if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    print(i)

"""DESSA FORMA ELE CUMPRE A REGRA MAS NÃO IMPRIME SE A PALAVRA TIVER EM MAIUSCULO"""
palavra2 = input("Digite a Palavra:"):

for i in palavra2:
  if i in 'aeiouAEIOU':
    print(i)

'''DESSA FORMA ELE IMPRIME TODAS OS ITENS QUE ESTIVEREM EM IN'''

palavra2 = input("Digite a Palavra:").lower():

for i in palavra2:
  if i in 'aeiou':
    print(i)

'''O LOWER TRANSFORMA TUDO EM MINUSCULO, FAZENDO COM QUE O IMPUTE FIQUE MINUSCULO E NÃO PRECISE TESTAR OS MAIUSCULOS'''