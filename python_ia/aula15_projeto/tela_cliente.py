"""
CRIE OS COMPONENTES PARA A INSERÇÃO DE:
- NOME
- TELEFONE
- EMAIL
- CPF

CRIE UM BOTÃO SALVAR, DEVE-SE RESGATAR AS INFORMAÇÕES DIGITADAS
E CRIAR UM OBJETO DO TIPO CLASSE CLIENTE


"""

from Cliente import Cliente
import flet


def main(page : flet.Page):

    page.tittle = "Cadastro de Cliente:"

    menu = flet.Text (value="Informe seus dados abaixo:", size=40)
    page.controls.append(menu)

    nome = flet.TextField (width=100, hint_text = "Nome:")
    page.controls.append(nome)

    telefone = flet.TextField (width=100, hint_text = "Telefone:")
    page.controls.append(telefone)

    email = flet.TextField (width=100, hint_text = "E-mail:")
    page.controls.append(email)

    cpf = flet.TextField (width=100, hint_text = "CPF:")
    page.controls.append(cpf)

    erro = flet.Text (value= "", color="red")
    page.controls.append(erro)


    def objeto(e):

        nome_inf = nome.value
        telefone_inf = telefone.value
        email_inf = email.value
        cpf_inf = cpf.value

        if nome_inf == "" or telefone_inf =="" or email_inf == "" or cpf_inf == "":
            erro.value = "Todos os campos devem ser preenchindos!"
            page.update()

        else:
            pessoa1 = Cliente(nome_inf,telefone_inf,email_inf,cpf_inf)
            page.clean()

            sucesso = flet.Text (value= "Cadastro Concluido!", color="green", size=50)
            page.controls.append(sucesso)

            dado1 = flet.Text(value = f"Nome: {pessoa1.nome}", size=30)
            page.controls.append(dado1)

            dado2 = flet.Text(value = f"Telefone: {pessoa1.telefone}", size=30)
            page.controls.append(dado2)

            dado3 = flet.Text(value = f"E-mail: {pessoa1.email}", size=30)
            page.controls.append(dado3)

            dado4 = flet.Text(value = f"CPF: {pessoa1.cpf}", size=30)
            page.controls.append(dado4)

            page.update()


        
    
    salvar = flet.ElevatedButton(text="Salvar", on_click= objeto)
    page.controls.append(salvar)

    page.update()


flet.app(target = main)