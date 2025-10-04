import flet



def main(page : flet.Page):

    login = flet.Text (value= "Login:", size= 30)

    page.controls.append(login)

    user_login = flet.TextField (width=100)
    page.controls.append(user_login)

    #Podemos Usar o hint_text = "VALOR" para mostrar o texto dentro do "imput"
    #user_login = flet.TextField (width=100, hint_text = "Login")

    senha= flet.Text (value= "Senha:", size= 30)
    page.controls.append(senha)

    user_senha = flet.TextField (width=100, password=True)
    #Usamos o Password = True para informar que esse espaço é uma senha e ocultar a digitação

    page.controls.append(user_senha)

    erro = flet.Text("", color ='red')
    page.controls.append(erro)
    page.update

    def logar(evento):
        login = "admin"
        senha = "admin"
        login_digitado = user_login.value
        senha_digitada = user_senha.value

        if login_digitado == login and senha_digitada == senha:    
            page.clean()
            
            sucesso = flet.Text("Logado com sucesso!", color="Green")
            page.controls.append(sucesso)
            page.update()

        else: 
            
            erro.value = "Login e/ou senha inválidos!"
            page.update()


        print(f'{login_digitado} - {senha_digitada}')
            


            

    entrar = flet.ElevatedButton(text="Entrar", on_click= logar)
    page.controls.append(entrar)

    page.update()


flet.app(target = main)
