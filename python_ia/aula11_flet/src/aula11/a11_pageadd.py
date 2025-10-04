import flet

def main ( page: flet.Page):
    page.title = "Estilização Básica"

    page.add(
        flet.Text("Cor Personalizada", color = "Blue"),
        #SEMPRE SEPARAR OS COMPONENTES QUE VÃO SER ADICIONADOS COM ","
        flet.ElevatedButton("Botão estiloso", bgcolor= "Red", color = "white")
    )

flet.app(target=main)