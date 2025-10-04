import flet

def main(page: flet.Page):
    ola = flet.Text(value = "Olá Mundo!", size=30)
    page.controls.append(ola)
    page.update()


flet.app(target = main)
