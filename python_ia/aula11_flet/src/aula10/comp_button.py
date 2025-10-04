import flet

def main(page: flet.Page):
    ola = flet.Text(value = "Olá Mundo!", size=30)
    page.controls.append(ola)
    botao = flet.ElevatedButton ("Entrar")
    page.controls.append(botao)

    page.update()


flet.app(target = main)