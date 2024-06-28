import flet as ft
#from modelo import Division
#from modelo import Responsable

def main(page: ft.Page):
    page.window_width = 500
    page.window_height = 600
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(title=ft.Text("Nuevo registro"),
                       center_title=True,
                       bgcolor="blue",
                       color="white")

    txtResponsable = ft.TextField(label="Número de empleado")
    etiqueta = ft.Text("(Todo en mayúscula)", size=12, text_align="center", width=500) #page.window_width
    txtNombre = ft.TextField(label="Nombre")
    opciones = [ft.dropdown.Option("Doctorado")]
    drpGrado = ft.Dropdown(label="Seleccione su grado",
                           options=opciones)
    txtCorreo = ft.TextField(label="Correo")
    # Cargar las Divisiones de la base de datos
    #divisiones = Division.select()
    #options_divisiones = []
    #for d in divisiones:
    #    option = ft.dropdown.Option(text=d.id_division)
    #    lista.append(option)

    drpDivision =ft.Dropdown(label="Seleccione su División",
                             options=None)
    btnGuardar = ft.ElevatedButton("Guardar",
                                   icon="save",
                                   bgcolor="green",
                                   color="white",
                                   on_click=None)
    btnCancelar = ft.ElevatedButton("Cancelar",
                                   icon="close",
                                   bgcolor="red",
                                   color="white",
                                   on_click=None)
    rowBotones = ft.Row([btnGuardar,btnCancelar],
                        alignment="center")

    page.add(txtResponsable)
    page.add(etiqueta)
    page.add(txtNombre)
    page.add(drpGrado)
    page.add(txtCorreo)
    page.add(drpDivision)
    page.add(rowBotones)
    # Esta debe se la última línea de la función
    # Sirve para actualizar el formulario
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
