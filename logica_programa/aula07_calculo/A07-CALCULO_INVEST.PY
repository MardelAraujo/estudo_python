

print("--------CALCULO INVESTIMENTO--------")

aporte = float(input("Informe o aporte inicial do investimento:"))

tempo = int(input("Informe o tempo de investimento em meses:"))

print("--------RETORNO--------")

retorno = aporte

for i in range(tempo):

    retorno = 0.6* retorno /100 + retorno

print(f'Poupança:{retorno}')
    
retorno = aporte

'''VAMOS PRECISAR DE UMA VARIÁVEL AUXILIAR PARA ARMAZENAR O NOVO VALOR A CADA MÊS, 
ESSA VARIÁVEL É O RETORNO, QUE DIZ O RETORNO DO INVESTIMENTO A CADA MÊS'''

for i in range(tempo):

    retorno = 0.9* retorno /100 + retorno

print(f'BPC:{retorno}')

retorno = aporte

for i in range(tempo):

    retorno = 1.2* retorno /100 + retorno

print(f'FII:{retorno}')