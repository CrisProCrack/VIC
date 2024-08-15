from flet import *
import base64
import cv2
import threading

cap = cv2.VideoCapture(0)

class Conteo(UserControl):
    def __init__(self):
        super().__init__()
        self.img = Image(border_radius=border_radius.all(20))
        self.should_update = True

    def did_mount(self):
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.should_update = False

    def update_timer(self):
        while self.should_update:
            _, frame = cap.read()
            _, im_arr = cv2.imencode('.png', frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        return self.img

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

        def slider_changed(e):
            print(f"Slider changed to {e.control.value}")

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
                            Card(
                                elevation=30,
                                content=Container(
                                    bgcolor=colors.WHITE24,
                                    padding=10,
                                    border_radius=border_radius.all(20),
                                    content=Column([
                                        Conteo(),
                                        Text("OpenCV con Flet",
                                            size=20, weight="bold",
                                            color=colors.BLACK),
                                    ])
                                )
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
                            Card(
                                elevation=30,
                                content=Container(
                                    bgcolor=colors.WHITE24,
                                    padding=10,
                                    border_radius=border_radius.all(20),
                                    content=Column([
                                        Slider(min=500, max=900, on_change=slider_changed),
                                        Slider(min=500, max=900, on_change=slider_changed),
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
            ),
            expand=True
        )

def main(page: Page):
    page.title = "OpenCV con Flet"
    page.theme_mode = ThemeMode.LIGHT
    page.padding = 50
    page.window_left = page.window_left + 100
    
    aplicacion_view = AplicacionView(page)
    page.add(aplicacion_view)


    app(target=main)
    cap.release()
    cv2.destroyAllWindows()