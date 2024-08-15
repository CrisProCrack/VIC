from flet import *

class ConfiguracionView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):
        
        content = Column(
        [
            Text(
                "Configuración",
                theme_style=TextThemeStyle.HEADLINE_LARGE,
            ),
            Text("Usuario",
                    style=TextThemeStyle.TITLE_LARGE,
                    weight=FontWeight.BOLD),
            Text("Cambiar contraseña",
                    style=TextThemeStyle.BODY_LARGE,
                ),
            Row(
                [
                    TextField(
                        label="Contraseña nueva", 
                        width=250),
                    TextField(
                        label="Repetir contraseña", 
                        width=250),
                    ElevatedButton(
                        "Cambiar", 
                        bgcolor=colors.BLACK, 
                        color=colors.WHITE),
                ],
                alignment=MainAxisAlignment.START,
            ),
            Divider(),
            Text("Aplicación", 
                style=TextThemeStyle.TITLE_LARGE, 
                weight=FontWeight.BOLD),
            Row(
                [
                    Text("Seleccionar cámaras disponibles",
                        style=TextThemeStyle.BODY_LARGE
                        ),
                    Dropdown(
                        width=260,
                        options=[
                            dropdown.Option("Opción 1"),
                            dropdown.Option("Opción 2"),
                        ],
                    ),
                    Container(width=1),
                    Container(width=1),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Row(
                [
                    Text("Brillo",
                            style=TextThemeStyle.BODY_LARGE,
                        ),
                    Slider(min=0, max=100, divisions=2, width=300),
                    Container(width=1),
                    
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        spacing=20,
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