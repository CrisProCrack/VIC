from flet import *

class AyudaView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):
    
        ayuda_contenedor = Container(
            content=Row(
                [
                    Container(
                        width=100,
                        height=100,
                        border=border.all(1, colors.BLACK),
                        content=Icon(icons.CLOSE),
                        alignment=alignment.center,
                    ),
                    Column(
                        [
                            Text(
                                "Nisi quis",
                                theme_style=TextThemeStyle.TITLE_LARGE,
                            ),
                            Text(
                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
                                "eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                                theme_style=TextThemeStyle.BODY_MEDIUM,
                            ),
                        ],
                        spacing=10,
                        expand=True,
                    ),
                ],
                spacing=20,
            ),
            bgcolor=colors.GREY_300,
            padding=20,
            border_radius=10,
            margin=margin.only(bottom=10),
        )
        
        ayuda_lista = [ayuda_contenedor for _ in range(5)]
        
        content = ListView(
            [
                Text(
                    "Ayuda",
                    theme_style=TextThemeStyle.HEADLINE_LARGE,
                ),
                *ayuda_lista,
            ],
            spacing=20,
            expand=True,
        )

        return Row(
            [
                Container(
                    content=content,
                    expand=True,
                )
            ],
            expand=True,
        )