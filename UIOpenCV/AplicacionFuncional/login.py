from flet import *

class LoginView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):
        def login(e):
            if not self.page.username or not self.page.password:
                self.username.error_text = "Por favor ingrese un nombre de usuario"
                self.update()
            elif not self.password.value:
                self.password.error_text = "Por favor ingrese una contraseña"
                self.update()
            else:
                self.username.error_text = ""
                self.password.error_text = ""
                self.page.go("/aplicacion")
    
        self.username = TextField(label="Usuario", width=200)
        self.password = TextField(label="Contraseña", password=True, can_reveal_password=True, width=200)
        submit = ElevatedButton(text="Iniciar sesión", on_click=login, width=300)
        
        login_card = Card(
            content= Container(
                content= Column(
                    [
                        Text("Iniciar sesión", style=TextThemeStyle.TITLE_LARGE),
                        self.username,
                        self.password,
                        submit,
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                width=400,
                padding=30,
            )
        )
        
        return Container(
            content=login_card,
            alignment=alignment.center
        )
            