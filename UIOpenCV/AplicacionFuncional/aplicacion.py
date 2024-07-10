from flet import *

class AplicacionView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):
        def dropdown_changed(e):
            print(f"Dropdown 1 changed to {e.control.value}")
        
        def dropdown2_changed(e):
            print(f"Dropdown 2 changed to {e.control.value}")
        
        def dropdown3_changed(e):
            print(f"Dropdown 3 changed to {e.control.value}")

        dropdown1 = Dropdown(
            width=200,
            options=[
                dropdown.Option("Opción 1"),
                dropdown.Option("Opción 2"),
                dropdown.Option("Opción 3"),
            ],
            on_change=dropdown_changed
        )
        
        dropdown2 = Dropdown(
            width=200,
            options=[
                dropdown.Option("Opción A"),
                dropdown.Option("Opción B"),
                dropdown.Option("Opción C"),
            ],
            on_change=dropdown2_changed
        )
        
        dropdown3 = Dropdown(
            width=200,
            options=[
                dropdown.Option("Opción A"),
                dropdown.Option("Opción B"),
                dropdown.Option("Opción C"),
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
    
        
        return Container(
            content=Row(
                [
                    Container(
                        content=rail,
                        expand=True
                    ),
                    VerticalDivider(width=1),
                    Column(
                        [
                            Text("Aplicación", theme_style=TextThemeStyle.DISPLAY_LARGE),
                            Container(height=53),
                            Container(
                                alignment=alignment.center,
                                bgcolor=colors.AMBER,
                                width=284,
                                height=220,
                                border_radius=10,
                            ),
                            Container(height=10),
                            Text(
                                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                                theme_style=TextThemeStyle.BODY_LARGE,
                                width=284,
                                height=220,
                                text_align=TextAlign.JUSTIFY,
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
                            Slider(width=300),
                            Container(height=20),
                            dropdown3,
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        expand=True,
                    ),
                ],
                expand=True,
            ),
            expand=True
        )