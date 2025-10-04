'''
Usando flet, crie uma calculadora simples
A calculadora terá dois campos de entrada para o usuário
e um botão com o texto '+' representando adição.
quando o usuário clicar no botao, deve-se somar os valores do texto
e apresentar para o usuário em outro texto
'''

import flet



def main(page:flet.Page):

    page.tittle = "CALCULADORA:"


    menu = flet.Text (value="Informe os numeros abaixo:", size=30)
    page.controls.append(menu)

    num1 = flet.TextField (width=100, hint_text = "Valor 1:")
    page.controls.append(num1)

    num2 = flet.TextField (width=100, hint_text = "Valor 2:")
    page.controls.append(num2)


    erro = flet.Text (value= "", color="red")
    page.controls.append(erro)

    sucesso = flet.Text(value="", color= "Green")
    page.controls.append(sucesso)

    def soma(e):
        
# SEMPRE QUE FIZERMOS UMA FUNÇÃO QUE É LIGADA A UM BOTÃO DEVEMOS CRIAR OS COMPONENTES FORA 
# PARA QUE NÃO FIQUE REPETINDO TODA VEZ QUE CLICARMOS NO BOTÃO

        if num1.value == "" or num2.value == "":
            erro.value = "Todos os campos devem ser preenchindos!"
            page.update()

        else:
            num1_inf = int(num1.value)
            num2_inf = int(num2.value)

            resultado = num1_inf + num2_inf
            sucesso.value = f'O resultado é: {resultado}'
            page.controls.append(sucesso)
            page.update()
            
    
    somar = flet.ElevatedButton(text="+", on_click= soma)
    page.controls.append(somar)

    page.update()

               


flet.app(target = main)