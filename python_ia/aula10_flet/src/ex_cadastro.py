import flet

def main(page:flet.Page):

    page.tittle = "Cadastro Pessoa Física:"


    menu = flet.Text (value="Informe seus dados abaixo:", size=30)
    page.controls.append(menu)

    nome = flet.TextField (width=100, hint_text = "Nome:")
    page.controls.append(nome)

    cpf = flet.TextField (width=100, hint_text = "CPF:")
    page.controls.append(cpf)

    telefone = flet.TextField (width=100, hint_text = "Telefone:")
    page.controls.append(telefone)

    erro = flet.Text (value= "", color="red")
    page.controls.append(erro)

    def teste(e):
        
        nome_inf = nome.value
        cpf_inf = cpf.value
        telefone_inf = telefone.value

        if nome_inf == "" or cpf_inf == "" or telefone_inf == "":
            erro.value = "Todos os campos devem ser preenchindos!"
            page.update()

        else:
            page.clean()
            sucesso = flet.Text (value= "Cadastro Concluido!", color="green")
            page.controls.append(sucesso)
            page.update()
            
    
    entrar = flet.ElevatedButton(text="Entrar", on_click= teste)
    page.controls.append(entrar)

    page.update()
               


flet.app(target = main)
   