import flet as ft
from flet import *

def main(page: Page):
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
                ],
                alignment=MainAxisAlignment.START, 
                expand=True
                )
        ],
            expand=True,
        )
        
    )
    
if __name__ == "__main__":
    ft.app(target=main)