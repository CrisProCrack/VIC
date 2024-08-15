from flet import *

class UsuarioView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    def build(self):
        
        profile_pic = Container(
            content=Icon(icons.ACCOUNT_CIRCLE, size=180,color=colors.BLACK),
            width=180,
            height=180,
        )
        
        user_info = Column(
        [
            profile_pic,
            TextButton("Actualizar foto de perfil"),
            Container(height=10),
            TextField(label="Nombre"),
            TextField(label="Género"),
            TextField(label="Fecha de nacimiento"),
        ],
        spacing=10,
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )
        header_usuario = Column(
        [
            Text(
                "Usuario",
                style=TextThemeStyle.DISPLAY_LARGE,
            ),
            Container(
                content=user_info,
                expand=True,
                alignment=alignment.center,
            )
        ],
        expand=True,
    )
        return Row(
            [
                header_usuario,
            ],
            expand=True,
        )