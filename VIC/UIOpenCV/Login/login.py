import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_50

    def login(e):
        if not username.value:
            username.error_text = "Por favor ingrese un nombre de usuario"
            page.update()
        elif not password.value:
            password.error_text = "Por favor ingrese una contraseña"
            page.update()
        else:
            username.error_text = ""
            password.error_text = ""
            page.clean()
            page.add(ft.Text(f"¡Bienvenido, {username.value}!"))

    username = ft.TextField(label="Usuario", width=300)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    submit = ft.ElevatedButton(text="Iniciar sesión", on_click=login, width=300)

    login_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("quam vulputate dignissim suspendisse in", size=30, weight=ft.FontWeight.BOLD),
                    username,
                    password,
                    submit
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            width=400,
            padding=30,
        )
    )

    page.add(login_card)

ft.app(target=main)