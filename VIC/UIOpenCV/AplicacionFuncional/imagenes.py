# imagenes.py
from flet import *
import cv2
import numpy as np
import base64

def to_base64(image):
    base64_image = cv2.imencode('.png', image)[1]
    base64_image = base64.b64encode(base64_image).decode('utf-8') 
    return base64_image

class ImagenesView(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.image = None
        
        # Create a blank image for the initial display
        init_image = np.zeros((480, 640, 3), dtype=np.uint8) + 128
        init_base64_image = to_base64(init_image)
        
        self.image_src = Image(
            src_base64=init_base64_image, 
            width=640, 
            height=480)
        self.image_dst = Image(
            src_base64=init_base64_image, 
            width=640, 
            height=480)
        
        self.file_picker = FilePicker(on_result=self.on_file_selected)
        self.page.overlay.append(self.file_picker)

    def build(self):
        return Container(
            content=Column([
                Text("Imágenes", theme_style=TextThemeStyle.DISPLAY_LARGE),
                ElevatedButton("Selecciona la imagen", on_click=self.on_click),
                Row(
                    [
                    self.image_src, 
                    self.image_dst
                    ]),
                Row(
                    [
                        ElevatedButton("Detección de bordes", on_click=self.edge_detection),
                        ElevatedButton("Detección de características", on_click=self.feature_detection),
                    ]),
            ]),
            expand=True
        )

    def edge_detection(self, e):
        if self.image is None:
            return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 10, 200)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        base64_image = to_base64(edges)
        self.image_dst.src_base64 = base64_image
        self.image_dst.update()
        
    def feature_detection(self, e):
        if self.image is None:
            return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
        if corners is not None:
            for x, y in np.uint(corners).reshape(-1, 2):
                cv2.circle(self.image, (x, y), 10, (0, 255, 0), 1)
        base64_image = to_base64(self.image)
        self.image_dst.src_base64 = base64_image
        self.image_dst.update()

    def on_file_selected(self, e: FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            print("archivo seleccionado :", file_path)
            self.image = cv2.imread(file_path)
            base64_image = to_base64(self.image)
            self.image_src.src_base64 = base64_image
            self.image_src.update()

    def on_click(self, e):
        self.file_picker.pick_files(allow_multiple=False, 
                                    file_type=FilePickerFileType.IMAGE)