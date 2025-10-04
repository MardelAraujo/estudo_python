'''PEÇA AO UZUÁRIO PARA INSERIR 2 NUMERO
USE O LAÇO FOR PARA CONTAR QUANTOS SÃO
POSITIVOS E QUANTOS SÃO NEGATIVOS ENTRE O INCIO E O FIM
imprima quantos numero pares e impares possui no intervalo'''


inicio = int(input("Infome o inicio:"))
fim = int(input("Infome o fim:"))

pares = 0
impares = 0

for i in range(inicio,fim+1):
    if i % 2 == 0:
        pares += 1
    else:
        impares +=1
    
print(f'O intervalo possui {pares} números pares e {impares} numeros impares.')