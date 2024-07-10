from flet import *

class ConfiguracionView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):
        rail = NavigationRail(
            selected_index=5,
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
            on_change=lambda e: self.page.go(f"/{e.control.selected_index}"),
        )
        
        content = Column(
        [
            Text(
                "Configuración",
                theme_style=TextThemeStyle.HEADLINE_LARGE,
            ),
            Text("Usuario",
                    style=TextThemeStyle.TITLE_LARGE,
                    weight=FontWeight.BOLD),
            Text("Cambiar contraseña",
                    style=TextThemeStyle.BODY_LARGE,
                ),
            Row(
                [
                    TextField(
                        label="Contraseña nueva", 
                        width=250),
                    TextField(
                        label="Repetir contraseña", 
                        width=250),
                    ElevatedButton(
                        "Cambiar", 
                        bgcolor=colors.BLACK, 
                        color=colors.WHITE),
                ],
                alignment=MainAxisAlignment.START,
            ),
            Divider(),
            Text("Aplicación", 
                 style=TextThemeStyle.TITLE_LARGE, 
                 weight=FontWeight.BOLD),
            Row(
                [
                    Text("Seleccionar cámaras disponibles",
                        style=TextThemeStyle.BODY_LARGE
                        ),
                    Dropdown(
                        width=260,
                        options=[
                            dropdown.Option("Opción 1"),
                            dropdown.Option("Opción 2"),
                        ],
                    ),
                    Container(width=1),
                    Container(width=1),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            Row(
                [
                    Text("Brillo",
                            style=TextThemeStyle.BODY_LARGE,
                        ),
                    Slider(min=0, max=100, divisions=2, width=300),
                    Container(width=1),
                    
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        spacing=20,
    )
    
        return Row(
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