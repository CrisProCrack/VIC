import flet as ft
from flet import *
import base64
import cv2

cap = cv2.VideoCapture(0)

class Conteo(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def did_mount(self):
        self.update_timer()
    
    def update_timer(self):
        while True:
            _, frame = cap.read()
            _, im_arr = cv2.imencode('.png', frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()
    
    def build(self):
        self.img = ft.Image(
            border_radius=ft.border_radius.all(20)
        )
        return self.img

def main(page: Page):
    def dropdown_changed(e):
        print(f"Dropdown 1 changed to {e.control.value}")

    def dropdown2_changed(e):
        print(f"Dropdown 2 changed to {e.control.value}")

    def dropdown3_changed(e):
        print(f"Dropdown 3 changed to {e.control.value}")

    def height_changed(e):
        print(f"Slider changed to {e.control.value}")

    dropdown1 = Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Opción 1"),
            ft.dropdown.Option("Opción 2"),
            ft.dropdown.Option("Opción 3"),
        ],
        on_change=dropdown_changed
    )

    dropdown2 = Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Opción A"),
            ft.dropdown.Option("Opción B"),
            ft.dropdown.Option("Opción C"),
        ],
        on_change=dropdown2_changed
    )

    dropdown3 = Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Opción A"),
            ft.dropdown.Option("Opción B"),
            ft.dropdown.Option("Opción C"),
        ],
        on_change=dropdown3_changed
    )

    rail = NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.CREATE, text="Añadir"),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.HOME_SHARP,
                selected_icon=icons.HOME,
                label="Inicio"
            ),
            NavigationRailDestination(
                icon=icons.LINKED_CAMERA_ROUNDED,
                selected_icon=icons.LINKED_CAMERA,
                label="Aplicación"
            ),
            NavigationRailDestination(
                icon=icons.ACCOUNT_CIRCLE_SHARP,
                selected_icon=icons.ACCOUNT_CIRCLE,
                label="Usuarios"
            ),
            NavigationRailDestination(
                icon=icons.BAR_CHART_OUTLINED,
                selected_icon=icons.BAR_CHART,
                label="Estadísticas"
            ),
            NavigationRailDestination(
                icon=icons.HELP_SHARP,
                selected_icon=icons.HELP,
                label="Ayuda"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_SHARP,
                selected_icon=icons.SETTINGS,
                label="Configuración"
            ),
            NavigationRailDestination(
                icon=icons.EXIT_TO_APP_SHARP,
                selected_icon=icons.EXIT_TO_APP,
                label="Salir"
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column(
                    [
                        Text("Aplicación", theme_style=ft.TextThemeStyle.DISPLAY_LARGE),
                        Container(height=53),
                        Card(
                            elevation=30,
                            content=Container(
                                bgcolor=ft.colors.WHITE24,
                                padding=10,
                                border_radius=ft.border_radius.all(20),
                                content=Column([
                                    Conteo(),
                                    Text("OpenCV con Flet",
                                        size=20, weight="bold",
                                        color=ft.colors.BLACK),
                                ])
                            )
                        ),
                        Container(height=10),
                        Text(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                            theme_style=ft.TextThemeStyle.BODY_LARGE,
                            width=284,
                            height=220,
                            text_align=ft.TextAlign.JUSTIFY,
                        ),
                        Container(expand=True),
                    ],
                    expand=True,
                    alignment=MainAxisAlignment.START,
                ),
                Column(
                    [
                        Container(
                            content=Column([
                                dropdown1,
                                Container(height=20),
                                dropdown2,
                            ]),
                            alignment=alignment.center,
                        ),
                        Card(
                            elevation=30,
                            content=Container(
                                bgcolor=ft.colors.WHITE24,
                                padding=10,
                                border_radius=ft.border_radius.all(20),
                                content=Column([
                                    Slider(min=500, max=900, on_change=height_changed),
                                    Slider(min=500, max=900, on_change=height_changed),
                                ])
                            )
                        ),
                        Container(height=20),
                        dropdown3,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )

    page.padding = 50
    page.window_left = page.window_left + 100
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'OpenCV con Flet'

if __name__ == "__main__":
    ft.app(target=main)
    cap.release()
    cv2.destroyAllWindows()