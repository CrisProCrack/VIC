import flet as ft

# Lista para almacenar los clientes
data = []

def main(page: ft.Page):
    page.title = "Login"
    page.bgcolor = ft.colors.WHITE  # Fondo blanco
    
    # Crear campos de texto para iniciar sesión
    username = ft.TextField(label="Usuario", width=300, text_style=ft.TextStyle(color=ft.colors.BLACK))
    password = ft.TextField(label="Contraseña", password=True, width=300, text_style=ft.TextStyle(color=ft.colors.BLACK))
    
    # Mensaje de estado
    status = ft.Text(value="", color=ft.colors.RED)

    # Función para el botón de inicio de sesión
    def login_click(e):
        if username.value == "Angel" and password.value == "Nopasar2025":
            status.value = "Inicio de sesión exitoso"
            status.color = ft.colors.GREEN
            # Limpiar la interfaz de inicio de sesión
            page.controls.clear()  
            # Mostrar la interfaz de CRUD
            page.add(crud_container())  
            page.update()
        else:
            status.value = "Usuario o contraseña incorrectos"
            status.color = ft.colors.RED
            page.update()

    # Botón de login
    login_button = ft.FilledButton("Iniciar sesión", on_click=login_click, style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_100))

    # Barra horizontal
    barra = ft.Container(
        content=ft.Text("Iniciar sesión", size=20, weight="bold", color=ft.colors.WHITE),
        bgcolor=ft.colors.GREEN_200, 
        padding=10,
        width=page.window_width,
        alignment=ft.alignment.center,
    )

    # Añadir los componentes a la página
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

    # Función para crear la interfaz de CRUD
    def crud_container():
        # Campos para los datos del cliente
        id_cliente_input = ft.TextField(label="ID Cliente", width=100, text_style=ft.TextStyle(color=ft.colors.BLACK))
        nombre_input = ft.TextField(label="Nombre", width=200)
        pago_input = ft.TextField(label="Pago", width=100)
        fecha_compra_input = ft.TextField(label="Fecha de Compra (YYYY-MM-DD)", width=150)
        telefono_input = ft.TextField(label="Teléfono", width=100)
        correo_input = ft.TextField(label="Correo Electrónico", width=200)
        direccion_input = ft.TextField(label="Dirección", width=200)
        usuario_input = ft.TextField(label="Usuario", width=100)
        c_password_input = ft.TextField(label="Confirmar Contraseña", password=True, width=150)

        add_button = ft.FilledButton("Agregar", on_click=lambda e: add_item(), style=ft.ButtonStyle(bgcolor=ft.colors.GREEN_100))
        item_list = ft.Column(scroll=True)  # Permitir desplazamiento en la columna

        # Función para agregar un elemento
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

        # Función para limpiar los campos de entrada
        def clear_inputs():
            id_cliente_input.value = ""
            nombre_input.value = ""
            pago_input.value = ""
            fecha_compra_input.value = ""
            telefono_input.value = ""
            correo_input.value = ""
            direccion_input.value = ""
            usuario_input.value = ""
            c_password_input.value = ""

        # Función para actualizar la lista de elementos
        def update_item_list():
            item_list.controls = []
            for index, item in enumerate(data):
                item_row = ft.Row(
                    controls=[
                        ft.Text(f"ID: {item['id_cliente']} | Nombre: {item['nombre']}", color=ft.colors.BLACK),  # Texto negro
                        ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e, index=index: edit_item(index)),  # Botón de editar
                        ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, index=index: remove_item(index))  # Botón de eliminar
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
                item_list.controls.append(item_row)
            page.update()

        # Función para editar un elemento
        def edit_item(index):
            # Cargar datos en los campos de entrada
            id_cliente_input.value = data[index]["id_cliente"]
            nombre_input.value = data[index]["nombre"]
            pago_input.value = data[index]["pago"]
            fecha_compra_input.value = data[index]["fecha_compra"]
            telefono_input.value = data[index]["telefono"]
            correo_input.value = data[index]["correo"]
            direccion_input.value = data[index]["direccion"]
            usuario_input.value = data[index]["usuario"]
            c_password_input.value = data[index]["c_password"]
            add_button.text = "Guardar"
            add_button.on_click = lambda e: save_item(index)  # Guardar el elemento editado
            page.update()

        # Función para guardar el elemento editado
        def save_item(index):
            if id_cliente_input.value and nombre_input.value:
                # Actualizar los datos en la lista
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
                clear_inputs()  # Limpiar los campos de entrada
                add_button.text = "Agregar"  # Cambiar de nuevo a "Agregar"
                add_button.on_click = add_item  # Restablecer la función
                update_item_list()  # Actualizar la lista
                page.update()

        # Función para eliminar un elemento
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
                ft.Row(
                    controls=[
                        id_cliente_input,
                        nombre_input,
                        pago_input,
                        fecha_compra_input,
                        telefono_input,
                        correo_input,
                        direccion_input,
                        usuario_input,
                        c_password_input
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                add_button,
                item_list,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

# Ejecutar la app
ft.app(target=main)