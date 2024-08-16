from flet import *
import base64
import cv2
import threading
import numpy as np

cap = cv2.VideoCapture(0)

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

class Conteo(UserControl):
    def __init__(self):
        super().__init__()
        self.img = Image(border_radius=border_radius.all(20))
        self.should_update = True
        self.image_filter = PREVIEW

    def did_mount(self):
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.should_update = False

    def update_timer(self):
        while self.should_update:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)

            if self.image_filter == PREVIEW:
                result = frame
            elif self.image_filter == CANNY:
                result = cv2.Canny(frame, 80, 150)
            elif self.image_filter == BLUR:
                result = cv2.blur(frame, (13, 13))
            elif self.image_filter == FEATURES:
                result = frame
                frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)
                if corners is not None:
                    for x, y in np.uint(corners).reshape(-1, 2):
                        cv2.circle(result, (x, y), 10, (0, 255, 0), 1)

            _, im_arr = cv2.imencode('.png', result)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        return self.img

class AplicacionView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.conteo = Conteo()
    
    def build(self):
        def dropdown_changed(e):
            filter_value = e.control.value
            if filter_value == "Normal":
                self.conteo.image_filter = PREVIEW
            elif filter_value == "Canny":
                self.conteo.image_filter = CANNY
            elif filter_value == "Blur":
                self.conteo.image_filter = BLUR
            elif filter_value == "Features":
                self.conteo.image_filter = FEATURES
            print(f"Filter changed to {filter_value}")

        dropdown1 = Dropdown(
            width=200,
            options=[
                dropdown.Option("Normal"),
                dropdown.Option("Canny"),
                dropdown.Option("Blur"),
                dropdown.Option("Features"),
            ],
            on_change=dropdown_changed
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
                                        self.conteo,
                                        Text("OpenCV con Flet",
                                            size=20, weight="bold",
                                            color=colors.BLACK),
                                    ])
                                )
                            ),
                            Container(height=10),
                            Text(
                                "Selecciona un filtro del menú desplegable para aplicarlo a la imagen en tiempo real.",
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
                                ]),
                                alignment=alignment.center,
                            ),
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

    page.on_close = lambda _: cap.release()

if __name__ == "__main__":
    app(target=main)