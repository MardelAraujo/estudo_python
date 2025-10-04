import flet

def main ( page: flet.Page):
    page.title = "Utilizando Temas"
    page.bgcolor = "white"

    #DEFININDO TEMA PERSONALIZADO

    theme = flet.Theme(
        color_scheme = flet.ColorScheme(
            primary= flet.colors.WHITE10,
            secondary= flet.colors.BLUE_200,
            background= flet.colors.BLACK87,
            surface= flet.colors.BLUE_100,
            on_primary= flet.colors.BLACK,
            on_secondary= flet.colors.BLACK,
            on_background= flet.colors.WHITE,
            on_surface= flet.colors.WHITE,
        ),
        font_family = "Arial"
    )
    page.add(
        flet.Text("Cor Personalizada", color = 'primary' ),
        #SEMPRE SEPARAR OS COMPONENTES QUE VÃO SER ADICIONADOS COM ","
        flet.ElevatedButton("Botão estiloso", bgcolor= "background", color = "surface")
    )

flet.app(target=main)