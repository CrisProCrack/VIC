import flet as ft

data = []

def main(page: ft.Page):
    page.title = "Login"
    page.bgcolor = ft.colors.WHITE
    page.scroll = "always"  # Enable scrolling for the entire page
    
    username = ft.TextField(label="Usuario", width=300, text_style=ft.TextStyle(color=ft.colors.BLACK))
    password = ft.TextField(label="Contraseña", password=True, width=300, text_style=ft.TextStyle(color=ft.colors.BLACK))
    
    status = ft.Text(value="", color=ft.colors.RED)

    def login_click(e):
        if username.value == "Angel" and password.value == "Nopasar2025":
            status.value = "Inicio de sesión exitoso"
            status.color = ft.colors.GREEN
            page.controls.clear()
            page.add(crud_container())
            page.update()
        else:
            status.value = "Usuario o contraseña incorrectos"
            status.color = ft.colors.RED
            page.update()

    login_button = ft.FilledButton("Iniciar sesión", on_click=login_click, style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_100))

    barra = ft.Container(
        content=ft.Text("Iniciar sesión", size=20, weight="bold", color=ft.colors.WHITE),
        bgcolor=ft.colors.GREEN_200, 
        padding=10,
        width=page.window_width,
        alignment=ft.alignment.center,
    )

    page.add(
        barra,
        ft.Container(
            content=ft.Column(
                controls=[
                    username,
                    password,
                    login_button,
                    status
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

    def crud_container():
        # Create input fields
        id_cliente_input = ft.TextField(label="ID Cliente", width=100, text_style=ft.TextStyle(color=ft.colors.BLACK))
        nombre_input = ft.TextField(label="Nombre", width=200)
        pago_input = ft.TextField(label="Pago", width=100)
        fecha_compra_input = ft.TextField(label="Fecha de Compra (YYYY-MM-DD)", width=150)
        telefono_input = ft.TextField(label="Teléfono", width=100)
        correo_input = ft.TextField(label="Correo Electrónico", width=200)
        direccion_input = ft.TextField(label="Dirección", width=200)
        usuario_input = ft.TextField(label="Usuario", width=100)
        c_password_input = ft.TextField(label="Confirmar Contraseña", password=True, width=150)

        # Create a horizontal scrollable row for input fields
        input_fields = ft.Container(
            content=ft.Row(
                controls=[
                    id_cliente_input,
                    nombre_input,
                    pago_input,
                    fecha_compra_input,
                    telefono_input,
                    correo_input,
                    direccion_input,
                    usuario_input,
                    c_password_input,
                ],
                scroll=ft.ScrollMode.AUTO,
                spacing=10,
            ),
            height=70,  # Adjust height as needed
            padding=ft.padding.all(10),
        )

        add_button = ft.FilledButton("Agregar", on_click=lambda e: add_item(), style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_100))
        item_list = ft.ListView(expand=1, spacing=10, padding=20)  # Use ListView for better performance

        def add_item():
            # Recoger datos de los campos
            id_cliente = id_cliente_input.value
            nombre = nombre_input.value
            pago = pago_input.value
            fecha_compra = fecha_compra_input.value
            telefono = telefono_input.value
            correo = correo_input.value
            direccion = direccion_input.value
            usuario = usuario_input.value
            c_password = c_password_input.value

            # Agregar datos a la lista
            if id_cliente and nombre:
                data.append({
                    "id_cliente": id_cliente,
                    "nombre": nombre,
                    "pago": pago,
                    "fecha_compra": fecha_compra,
                    "telefono": telefono,
                    "correo": correo,
                    "direccion": direccion,
                    "usuario": usuario,
                    "c_password": c_password,
                })
                clear_inputs()
                update_item_list()
                page.update()

        def clear_inputs():
            for control in input_fields.content.controls:
                if isinstance(control, ft.TextField):
                    control.value = ""

        def update_item_list():
            item_list.controls.clear()
            for index, item in enumerate(data):
                item_row = ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(f"ID: {item['id_cliente']} | Nombre: {item['nombre']}", color=ft.colors.BLACK),
                            ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, index=index: edit_item(index)),
                            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, index=index: remove_item(index))
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    bgcolor=ft.colors.BLUE_50,
                    border_radius=5,
                    padding=5,
                )
                item_list.controls.append(item_row)
            page.update()

        def edit_item(index):
            # Cargar datos en los campos de entrada
            item = data[index]
            id_cliente_input.value = item["id_cliente"]
            nombre_input.value = item["nombre"]
            pago_input.value = item["pago"]
            fecha_compra_input.value = item["fecha_compra"]
            telefono_input.value = item["telefono"]
            correo_input.value = item["correo"]
            direccion_input.value = item["direccion"]
            usuario_input.value = item["usuario"]
            c_password_input.value = item["c_password"]
            add_button.text = "Guardar"
            add_button.on_click = lambda e: save_item(index)
            page.update()

        def save_item(index):
            if id_cliente_input.value and nombre_input.value:
                data[index] = {
                    "id_cliente": id_cliente_input.value,
                    "nombre": nombre_input.value,
                    "pago": pago_input.value,
                    "fecha_compra": fecha_compra_input.value,
                    "telefono": telefono_input.value,
                    "correo": correo_input.value,
                    "direccion": direccion_input.value,
                    "usuario": usuario_input.value,
                    "c_password": c_password_input.value,
                }
                clear_inputs()
                add_button.text = "Agregar"
                add_button.on_click = add_item
                update_item_list()
                page.update()

        def remove_item(index):
            del data[index]
            update_item_list()

        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("CRUD de Clientes", size=20, weight="bold"),
                    alignment=ft.alignment.center,
                    padding=10
                ),
                input_fields,
                add_button,
                item_list,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,  # Enable scrolling for the entire CRUD container
        )

ft.app(target=main)