import flet as ft
from flet import *

def main(page: Page):
    page.bgcolor = ft.colors.PINK_50

    rail = NavigationRail(
        selected_index=5,
        label_type=NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.HOME_SHARP, selected_icon=icons.HOME, label="Inicio"
            ),
            NavigationRailDestination(
                icon=icons.LINKED_CAMERA_ROUNDED, selected_icon=icons.LINKED_CAMERA, label="Aplicación"
            ),
            NavigationRailDestination(
                icon=icons.ACCOUNT_CIRCLE_SHARP, selected_icon=icons.ACCOUNT_CIRCLE, label="Usuarios"
            ),
            NavigationRailDestination(
                icon=icons.BAR_CHART_OUTLINED, selected_icon=icons.BAR_CHART, label="Estadísticas"
            ),
            NavigationRailDestination(
                icon=icons.HELP_SHARP, selected_icon=icons.HELP, label="Ayuda"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_SHARP, selected_icon=icons.SETTINGS, label="Configuración"
            ),
            NavigationRailDestination(
                icon=icons.EXIT_TO_APP_SHARP, selected_icon=icons.EXIT_TO_APP, label="Salir"
            ),
        ],
    )

    content = Column(
        [
            Text("Configuración", style=TextThemeStyle.DISPLAY_MEDIUM, weight=FontWeight.BOLD),
            Text("Usuario", style=TextThemeStyle.HEADLINE_MEDIUM, weight=FontWeight.BOLD),
            Text("Cambiar contraseña"),
            Row(
                [
                    TextField(label="Contraseña nueva", width=200),
                    TextField(label="Repetir contraseña", width=200),
                    ElevatedButton("Cambiar", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE),
                ],
                alignment=MainAxisAlignment.START,
            ),
            Divider(),
            Text("Aplicación", style=TextThemeStyle.HEADLINE_MEDIUM, weight=FontWeight.BOLD),
            Row(
                [
                    Text("Seleccionar cámaras disponibles"),
                    Dropdown(
                        width=200,
                        options=[
                            dropdown.Option("Opción 1"),
                            dropdown.Option("Opción 2"),
                        ],
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Row(
                [
                    Text("Brillo"),
                    Slider(min=0, max=100, value=50, width=300),
                    Icon(icons.BRIGHTNESS_LOW),
                    Icon(icons.BRIGHTNESS_HIGH),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        spacing=20,
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Container(content=content, expand=True, padding=20),
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)