import flet as ft
from flet import *

def main(page: Page):
    rail = NavigationRail(
        selected_index=4,
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
    
    ayuda_contenedor = Container(
        content=Row(
            [
                Container(
                    width=100,
                    height=100,
                    border=border.all(1, colors.BLACK),
                    content=Icon(icons.CLOSE),
                    alignment=alignment.center,
                ),
                Column(
                    [
                        Text(
                            "Nisi quis",
                            theme_style=TextThemeStyle.TITLE_LARGE,
                        ),
                        Text(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
                            "eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                            theme_style=TextThemeStyle.BODY_MEDIUM,
                        ),
                    ],
                    spacing=10,
                    expand=True,
                ),
            ],
            spacing=20,
        ),
        bgcolor=colors.GREY_300,
        padding=20,
        border_radius=10,
        margin=margin.only(bottom=10),
    )
    
    ayuda_lista = [ayuda_contenedor for _ in range(5)]

    content = ListView(
        [
            Text(
                "Ayuda",
                theme_style=TextThemeStyle.HEADLINE_LARGE,
            ),
            *ayuda_lista,
        ],
        spacing=20,
        expand=True,
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Container(
                    content=content,
                    expand=True,
                    
                )
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
    