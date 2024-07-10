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
        
    
        
        return Container(
            content=Row(
                [
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