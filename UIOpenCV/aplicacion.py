import flet as ft
from flet import *

def main(page: Page):
    def dropdown_changed(e):
        print(f"Dropdown 1 changed to {e.control.value}")
    def dropdown2_changed(e):
        print(f"Dropdown 2 changed to {e.control.value}")
    def dropdown3_changed(e):
        print(f"Dropdown 3 changed to {e.control.value}")

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
        on_change=dropdown2_changed
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
                        Container(height=53),  # Este contenedor empuja el contenido hacia abajo
                        Container
                        (
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.AMBER,
                        width=284,
                        height=220,
                        border_radius=10,
                        ),
                        Container(height=10),  # Espacio entre el texto y los dropdowns
                        # Aquí puedes agregar más contenido debajo del título "Aplicación"
                        Text(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 
                            theme_style=ft.TextThemeStyle.BODY_LARGE,
                            width=284,height=220,
                            text_align=ft.TextAlign.JUSTIFY),
                        Container(expand=True),  # Este contenedor empuja el contenido hacia arriba
                    ],
                    expand=True,
                    alignment=MainAxisAlignment.START,
                ),
                Column(
                    [
                        Container(
                            content=Column([
                                dropdown1,
                                Container(height=20),  # Espacio entre los dropdowns
                                dropdown2,
                            ]),
                            alignment=alignment.center,
                        ),
                        Slider(width=300,height=60),
                        # Aquí puedes agregar más contenido debajo del dropdown
                        # Por ejemplo:
                        # Container(
                        #     content=Text("Contenido adicional"),
                        #     margin=margin.only(top=20),
                        # ),
                        # Puedes seguir agregando más widgets aquí
                        Container(height=20),  # Espacio entre los dropdowns
                        dropdown3,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            expand=True,
        )
    )
    
if __name__ == "__main__":
    ft.app(target=main)