import flet as ft
from flet import *

def main(page: Page):
    page.bgcolor = ft.colors.PINK_50

    rail = NavigationRail(
        selected_index=2,
        label_type=NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
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
                label="Usuario"
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
    )

    profile_pic = Container(
        content=Icon(icons.ACCOUNT_CIRCLE, size=100, color=ft.colors.BLACK),
        width=100,
        height=100,
    )

    user_info = Column(
        [
            Text("Usuario", style=TextThemeStyle.HEADLINE_LARGE, weight=FontWeight.BOLD),
            profile_pic,
            TextButton("Actualizar foto de perfil"),
            TextField(label="Nombre"),
            TextField(label="Género"),
            TextField(label="Fecha de nacimiento"),
        ],
        spacing=20,
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Container(
                    content=user_info,
                    expand=True,
                    alignment=alignment.center,
                ),
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)